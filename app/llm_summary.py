import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_articles(articles: list[dict], question: str = "요즘 사회 이슈가 뭐야?"):
    content = "\n".join([f"{i+1}. {a['title']}: {a['content']}" for i, a in enumerate(articles)])
    prompt = f"다음 뉴스 기사들을 기반으로 {question}\n\n{content}\n\n요약:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']