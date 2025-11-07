import subprocess
import os

def ensure_wav_16k(input_path: str) -> str:
    """
    Converts input audio (wav/mp3/m4a/etc) to WAV 16k mono.
    Requires ffmpeg installed on system.
    """
    out_path = input_path + "_16k.wav"
    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-ac", "1",
        "-ar", "16000",
        out_path
    ]
    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return out_path
    except Exception as e:
        print(f"[AUDIO] Conversion error: {e}")
        return input_path
