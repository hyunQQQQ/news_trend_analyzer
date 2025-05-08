import requests
from bs4 import BeautifulSoup

def fetch_news_links(date: str, page: int, sid: int = 102):
    url = f"https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1={sid}&date={date}&page={page}"
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, "html.parser")
    links = []
    for a_tag in soup.select("ul.type06_headline a"):
        href = a_tag.get('href')
        if href and "read.naver" in href:
            links.append(href)
    return list(set(links))

def fetch_article_content(url: str):
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.select_one("#articleTitle")
    content = soup.select_one("#articleBodyContents")
    return {
        "title": title.get_text(strip=True) if title else "",
        "content": content.get_text(" ", strip=True) if content else ""
    }