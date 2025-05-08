import os
from groq import Groq
from api.apigroq import transcription



def main():
    
    content, title= transcription()
    
    output_path = os.path.join("resumos")
    os.makedirs(output_path, exist_ok=True)
    filename = f"Resumo {title[:-4]}.md"
    full_path = os.path.join(output_path, filename)
    
    
    with open(full_path, "w+", encoding="utf-8") as md:
        md.write(content)

    
if __name__ == "__main__":
    main()