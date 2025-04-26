from google import genai
import json


def GeminiApiRequest(text_file):
    try:
        # Neemt API key
        with open("SpeechToCV/API.json", "r") as api_file:
            file = json.load(api_file)
            API_KEY = file["geminiAPI"]

        # Neemt de
        with open(text_file) as file:
            MESSAGE = file.read()

        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                "Format the following into a concise CV, make sure to use markdown formatting.\n" + MESSAGE, text_file]
        )

        with open("SpeechToCV/result.md", "w") as file:
            # Verwijderd markdown code block
            file.write(response.text[12:-6])

        return response.text[12:-6]
    except Exception as error:
        print(f"Error in GeminiApiRequest: {error}")
        return None


def GeminiApiRequestAudio(audio_file_path):
    with open("SpeechToCV/API.json", "r") as api_file:
        file = json.load(api_file)
        API_KEY = file["geminiAPI"]

    client = genai.Client(api_key=API_KEY)

    myfile = client.files.upload(file=audio_file_path)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=["In this audio file you hear a employee (a blue colar worker) talking with their supervisor. Summarize what you hear in this interview report into a CV for the employee.", myfile]
    )

    return response.text[12:-6]


GeminiApiRequestAudio("SpeechToCV/Silence Wench.mp3")
