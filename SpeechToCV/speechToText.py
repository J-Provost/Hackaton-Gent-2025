import assemblyai as aai
import json


def speech_to_text(audio_file) -> str:
    with open("Hackaton-Gent-2025/API.json", "r") as api_file:
        file = json.load(api_file)
        API_KEY = file["assemblyAI"]

    aai.settings.api_key = API_KEY
    config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.slam_1)

    transcript = aai.Transcriber(config=config).transcribe(audio_file)

    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")
    return transcript.text
