from google import genai
import csv
import json


def buildingguide():
    with open('buildingguide\data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        MESSAGE = "\n".join([",".join(row) for row in reader])

    with open("API.json", "r") as api_file:
        file = json.load(api_file)
        API_KEY = file["geminiAPI"]


    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents="Convert the following into csv into a structered text seperated by person, and each person seperated by a semicolon.\n" + MESSAGE
    )

    print(MESSAGE)
    print(response.text)
    with open("result.txt", "w") as file:
        file.write(response.text)

    individuals = response.text.strip().split(";")

    for individual in individuals:
        if individual.strip():  # Ensure the string is not empty
            # Extract the name (everything before the first colon)
            name, data = individual.split(":", 1)
            name = name.strip()

            # Write the data to a file named after the person
            with open(f"buildingguide\{name}.txt", "w", encoding="utf-8") as file:
                file.write(data.strip())



buildingguide()
