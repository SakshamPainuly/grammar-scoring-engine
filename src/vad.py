# Dummy VAD for Windows (no webrtcvad needed)

def apply_vad(path: str) -> str:
    """
    Dummy VAD: simply return the input audio path.
    Real VAD can be added if running on Linux.
    """
    return path
