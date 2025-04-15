import requests
import config

headers = {
    "Authorization": f"Bearer {config.OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "너는 예의 바르고 감성적인 블로그 방문자야. 글을 읽고 공감 가는 댓글을 작성해줘."},
        {"role": "user", "content": "블로그 글: 오늘은 봄비가 촉촉히 내리는 하루였습니다. 따뜻한 커피 한 잔과 함께 조용히 창밖을 바라보았어요."}
    ]
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)

print("🔵 상태코드:", response.status_code)
print("📦 응답 본문:", response.text)

try:
    content = response.json()["choices"][0]["message"]["content"]
    print("✅ 생성된 댓글:", content)
except KeyError:
    print("❌ 'choices' 키가 없음. 에러 응답일 수 있음.")