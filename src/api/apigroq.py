from groq import Groq
from dotenv import load_dotenv
import os
from download import baixar_audio
load_dotenv()

api_key = os.getenv('GROQAPIKEY')

def transcription():
    url = input('')
    title = baixar_audio(url) 
    
    client = Groq(api_key=api_key)
    
    filename = open(os.path.dirname(__file__) + f"/audios/{title}", "rb" )
    transcript = client.audio.transcriptions.create(
        model="whisper-large-v3",
        file=filename
    ).text

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em análise de vídeos. Resuma o vídeo abaixo de forma completa e detalhada, incluindo todos os tópicos abordados do início ao fim. Mantenha a ordem cronológica dos eventos e explique claramente cada seção importante. Não resuma em poucas linhas — o objetivo é criar um resumo extenso que cubra todo o conteúdo do vídeo, incluindo exemplos, argumentos, dados apresentados, opiniões relevantes e conclusões. Use linguagem clara e acessível. Divida em seções, se necessário. Não omita partes importantes, mesmo que o vídeo seja longo."
                "Responda com formatação em Markdown",

            },
            {
                "role": "user", 
                "content": f"Descreva o seguinte video: {transcript}"
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return completion.choices[0].message.content, title
