import assemblyai as aai
import json


def speech_to_text(audio_file: str) -> str:
    "Neemt een string van audio path file en returned Text van de audio file"
    with open("Hackaton-Gent-2025/SpeechToCV/API.json", "r") as api_file:
        file = json.load(api_file)
        API_KEY = file["assemblyAI"]

    aai.settings.api_key = API_KEY
    config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.slam_1)

    transcript = aai.Transcriber(config=config).transcribe(audio_file)

    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")
    return transcript.text

text_transcript = speech_to_text("Hackaton-Gent-2025/SpeechToCV/Silence Wench.mp3")

print(text_transcript)
with open("Hackaton-Gent-2025/rapporten/text_transcript1.txt", "w") as file:
    file.write(text_transcript)