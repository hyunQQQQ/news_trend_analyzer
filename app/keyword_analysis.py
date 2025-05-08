from collections import Counter
from konlpy.tag import Okt

def extract_keywords(texts: list[str], top_n: int = 10):
    okt = Okt()
    words = []
    for text in texts:
        nouns = okt.nouns(text)
        words.extend(nouns)
    counts = Counter(words)
    return counts.most_common(top_n)