import os
from faster_whisper import WhisperModel

# -------------------------------------------------------
# ✅ Load Faster-Whisper model (Windows compatible)
# -------------------------------------------------------

MODEL_NAME = os.getenv("WHISPER_MODEL", "tiny")

print(f"[ASR] Loading FasterWhisper model: {MODEL_NAME} on CPU ...")
model = WhisperModel(MODEL_NAME, device="cpu")
print("[ASR] FasterWhisper Loaded ✅")


# -------------------------------------------------------
# ✅ Transcribe audio
# -------------------------------------------------------
def transcribe_audio(path: str) -> str:
    """
    Transcribe audio using Faster-Whisper (Windows-safe).
    """
    try:
        segments, info = model.transcribe(
            path,
            beam_size=1,      # deterministic + faster
            language="en"
        )

        text = " ".join(seg.text for seg in segments)
        return text.strip()

    except Exception as e:
        print(f"[ASR] Error during transcription: {e}")
        return ""
