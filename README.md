# 🎙️ Grammar Scoring Engine  
### **SHL Research Intern – Technical Assessment Submission**

A lightweight speech-to-score system that analyzes spoken English responses and outputs:

- **Transcript**
- **Grammar score**
- **Fluency score**
- **Overall communication score**
- **Diagnostics & feedback**

The system includes a **REST API (FastAPI)** and a **demo UI (Gradio)**.

---

## ✅ Features (Quick Summary)

- **ASR:** Faster-Whisper (tiny, CPU-optimized)  
- **Grammar Scoring:** Heuristics (capitalization, punctuation, repeated words, structure)  
- **Fluency:** Words/minute + filler penalty  
- **Aggregation:** Weighted scoring  
- **UI:** Gradio interface for audio scoring  
- **API:** FastAPI with `/score` endpoint  

---

## ✅ Tech Stack

- Python  
- FastAPI  
- Gradio  
- Faster-Whisper (ctranslate2 backend)  
- ffmpeg (optional)  
- Uvicorn, Requests  

---

## ✅ How It Works (Pipeline)

```
Audio
 → Preprocessing
 → ASR (Faster-Whisper)
 → Grammar Heuristics
 → Fluency Scoring
 → Weighted Aggregation
 → JSON Output
```

---

## ✅ API Usage

### **POST /score**

Upload `.wav` or `.mp3`:

```
curl -X POST http://127.0.0.1:8000/score \
  -F "audio=@sample.wav"
```

Example output:

```
{
  "overall": 90.3,
  "grammar": 90,
  "fluency": 94.4,
  "transcript": "The stale smell of old beer lingers...",
  "diagnostics": ["Contains double spaces."]
}
```

---

## ✅ Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Start backend:

```
uvicorn api.main:app --reload
```

Start UI:

```
python demo/app.py
```

Backend Docs → http://127.0.0.1:8000/docs  
UI → http://127.0.0.1:7860  

---

## ✅ Project Structure (Minimal)

```
api/          ← FastAPI backend
src/          ← ASR, grammar, fluency, scoring modules
demo/         ← Gradio UI
models/       ← Scoring config
```

---

## ✅ Scoring Logic (Brief)

- Grammar: heuristic rule violations  
- Fluency: WPM + filler detection  
- Pronunciation: placeholder constant  
- Final score = weighted sum (`scoring_config.json`)  

---

## ✅ Why This Approach (For SHL Reviewers)

- Lightweight and deployable  
- Cross-platform (Windows/Linux/Cloud)  
- Fast inference (CPU-only)  
- No heavy dependencies like Java  
- Research-friendly modular design  
- Complete pipeline: **ASR → NLP → Scoring → API → UI**  

---

## ✅ Future Enhancements

- Transformer-based grammar scoring  
- Pronunciation scoring via CTC alignment  
- Improved VAD (Silero/WebRTC)  
- Multi-speaker support  
