import sounddevice as sd
from kokoro import KPipeline

VOICE = "am_adam"
SAMPLE_RATE = 24000

_pipeline = None

def load_model():
    global _pipeline
    _pipeline = KPipeline(lang_code="a", device="cpu")

def speak(text: str) -> None:
    if _pipeline is None:
        load_model()

    for result in _pipeline(text, voice=VOICE):
        if result.audio is not None:
            sd.play(result.audio.numpy(), samplerate=SAMPLE_RATE)
            sd.wait()
