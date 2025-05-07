from groq import Groq
import os
from src.api.apigroq import transcription


def main():
    
    content, title= transcription()
    output_path = "resumos"
    os.makedirs(output_path, exist_ok=True)
    filename = f"resumo {title[:len(title)-4]}.md"
    with open(f"{output_path}{filename}", "w+", encoding="utf-8") as md:
        md.write(content)


if __name__ == "__main__":
    main()