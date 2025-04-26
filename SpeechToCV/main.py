from GeminiApiRequest import *
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

    markdown_content2 = GeminiApiRequestAudio("SpeechToCV/Silence Wench.mp3")
    if markdown_content2:
        toPDF(markdown_content2)
    else:
        raise ValueError(
            "markdown_content2 returned invalid value, namely" + markdown_content2)


main()
