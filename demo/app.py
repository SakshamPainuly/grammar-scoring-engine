import gradio as gr
import requests
import os

print("UI script loaded ✅")

API_BASE = os.getenv("API_BASE", "http://127.0.0.1:8000")


def score_audio(audio_file):
    print("score_audio called ✅")

    if audio_file is None:
        return {"error": "No audio provided"}

    if not os.path.exists(audio_file):
        return {"error": "File not found"}

    try:
        files = {"audio": ("input.wav", open(audio_file, "rb"), "audio/wav")}
        r = requests.post(f"{API_BASE}/score", files=files, timeout=120)
        return r.json()
    except Exception as e:
        return {"error": str(e)}


with gr.Blocks(title="Grammar Scoring Engine") as demo:
    gr.Markdown("## 🎙 Grammar Scoring Engine\nUpload or record audio.")
    audio = gr.Audio(sources=["microphone", "upload"], type="filepath", label="Audio")
    btn = gr.Button("Analyze")
    out = gr.JSON(label="Scores + Transcript")

    btn.click(score_audio, inputs=audio, outputs=out)


if __name__ == "__main__":
    print("Launching UI on http://127.0.0.1:7860 ✅")
    demo.launch(server_name="127.0.0.1", server_port=7860)
