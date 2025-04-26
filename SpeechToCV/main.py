from GeminiApiRequest import GeminiApiRequest
from toPDF import toPDF


def main():
    # Maak markdown file
    markdown_content = GeminiApiRequest("SpeechToCV/script.txt")
    # Converteer naar PDF:
    if markdown_content:
        toPDF(markdown_content)
    else:
        raise ValueError(
            "markdown_content returned invalid value, namely" + markdown_content)


main()
