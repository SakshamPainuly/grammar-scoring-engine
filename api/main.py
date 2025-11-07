from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.asr import transcribe_audio
from src.vad import apply_vad
from src.grammar import grammar_score
from src.scoring import aggregate_scores
from src.audio_utils import ensure_wav_16k
import tempfile
import os

app = FastAPI(title="Grammar Scoring Engine", version="1.0.0")


class ScoreResponse(BaseModel):
    overall: float
    grammar: float
    fluency: float
    transcript: str
    diagnostics: list[str]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/score", response_model=ScoreResponse)
async def score(audio: UploadFile = File(...)):
    # Save upload to a temp file
    suffix = ".wav" if audio.filename.lower().endswith(".wav") else ".mp3"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await audio.read())
        in_path = tmp.name

    try:
        # Normalize to WAV 16k mono
        wav_path = ensure_wav_16k(in_path)

        # Simple VAD to remove silences
        vad_path = apply_vad(wav_path)

        # ASR
        transcript = transcribe_audio(vad_path)

        # Grammar analysis (score 0..100 and list of messages)
        g_score, diagnostics = grammar_score(transcript)

        # Fluency proxy: words per minute and fillers
        words = len(transcript.strip().split())
        fillers = transcript.lower().count(" uh ") + transcript.lower().count(" um ")
        fluency = max(0.0, min(100.0, 60 + (words * 0.8) - fillers * 5))

        # Pronunciation proxy (fixed baseline 80 for now; easy to extend)
        pron = 80.0

        overall = aggregate_scores(g_score, fluency, pron)

        return JSONResponse(
            content={
                "overall": overall,
                "grammar": g_score,
                "fluency": fluency,
                "transcript": transcript,
                "diagnostics": diagnostics,
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        for p in (in_path,):
            try:
                if p and os.path.exists(p):
                    os.remove(p)
            except Exception:
                pass
