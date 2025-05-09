# News RAG Backend

FastAPI 기반 백엔드 서비스로 네이버 뉴스의 최신 기사를 실시간 수집하여
- 키워드 빈도 분석
- LLM(GPT) 기반 요약

기능을 제공합니다.

## 사용법

### 1. 설치
```bash
git clone https://github.com/your-username/news-rag-backend.git
cd news-rag-backend
pip install -r requirements.txt
```

### 2. OpenAI API 키 설정
`.env` 파일 생성
```
OPENAI_API_KEY=your-key-here
```

### 3. 서버 실행
```bash
bash run.sh
```

## API Endpoints

| Method | Endpoint | 설명 |
|:-|:-|:-|
| GET | `/crawl?date=YYYYMMDD&page=N` | 뉴스 기사 수집 |
| GET | `/keywords?date=YYYYMMDD&page=N` | 키워드 분석 |
| GET | `/summary?date=YYYYMMDD&page=N` | 요약 응답 |
| GET | `/health` | 상태 확인 |
