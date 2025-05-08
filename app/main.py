from fastapi import FastAPI
from app.news_scraper import fetch_news_links, fetch_article_content
from app.keyword_analysis import extract_keywords
from app.llm_summary import summarize_articles

app = FastAPI()

@app.get("/crawl")
def crawl(date: str, page: int = 1):
    links = fetch_news_links(date, page)
    articles = [fetch_article_content(url) for url in links]
    return {"count": len(articles), "articles": articles}

@app.get("/keywords")
def get_keywords(date: str, page: int = 1):
    links = fetch_news_links(date, page)
    articles = [fetch_article_content(url) for url in links]
    texts = [a['content'] for a in articles]
    keywords = extract_keywords(texts)
    return {"keywords": keywords}

@app.get("/summary")
def get_summary(date: str, page: int = 1):
    links = fetch_news_links(date, page)
    articles = [fetch_article_content(url) for url in links]
    summary = summarize_articles(articles)
    return {"summary": summary}

@app.get("/health")
def health():
    return {"status": "ok"}