from google import genai
import json


def GeminiApiRequest():
    with open("Hackaton-Gent-2025/SpeechToCV/API.json", "r") as api_file:
        file = json.load(api_file)
        API_KEY = file["geminiAPI"]

    with open("Hackaton-Gent-2025/SpeechToCV/script.txt") as file:
        MESSAGE = file.read()

    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents="Format the following into a concise CV, make sure to use markdown formatting.\n" + MESSAGE
    )

    print(response.text)
    with open("Hackaton-Gent-2025/SpeechToCV/result.md", "w") as file:
        file.write(response.text[12:-6])
