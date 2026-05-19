import tempfile
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav
import whisper

SAMPLE_RATE = 16000

_model = None

def load_model(size="base"):
    global _model
    _model = whisper.load_model(size)

def record(duration: int) -> np.ndarray:
    print(f"Recording for {duration}s...")
    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
    )
    sd.wait()
    return audio

def transcribe(duration: int = 5) -> str:
    if _model is None:
        load_model()

    audio = record(duration)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, SAMPLE_RATE, audio)
        result = _model.transcribe(f.name, fp16=False, language="en")

    return result["text"].strip()
