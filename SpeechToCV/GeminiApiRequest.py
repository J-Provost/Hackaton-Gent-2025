from google import genai
import json


def GeminiApiRequest(text_file):
    with open("Hackaton-Gent-2025/SpeechToCV/API.json", "r") as api_file:
        file = json.load(api_file)
        API_KEY = file["geminiAPI"]

    with open("Hackaton-Gent-2025/SpeechToCV/script.txt") as file:
        MESSAGE = file.read()

    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=["Format the following into a concise CV, make sure to use markdown formatting.\n" + MESSAGE, text_file]
    )

    print(response.text)
    with open("Hackaton-Gent-2025/SpeechToCV/result.md", "w") as file:
        file.write(response.text[12:-6])

def GeminiApiRequestAudio(audio_file_path):
    with open("Hackaton-Gent-2025/SpeechToCV/API.json", "r") as api_file:
        file = json.load(api_file)
        API_KEY = file["geminiAPI"]

    client = genai.Client(api_key=API_KEY)

    myfile = client.files.upload(file=audio_file_path)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=["In this audio file you hear a employee (a blue colar worker) talking with their supervisor. Summarize what you hear in this interview report into a CV for the employee.", myfile]
    )

    return response.text[12:-6]
    # print(response.text)
    # with open("Hackaton-Gent-2025/SpeechToCV/result.md", "w") as file:
    #     file.write(response.text[12:-6])

GeminiApiRequestAudio("Hackaton-Gent-2025/SpeechToCV/Silence Wench.mp3")