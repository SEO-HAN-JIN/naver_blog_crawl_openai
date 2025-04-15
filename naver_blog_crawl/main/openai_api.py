import requests
import config

class OpenAiIntegration:
    def __init__(self):
        self.api_key = config.OPENAI_API_KEY
    
    def send_to_openai(self, contnet):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "너는 블로거야. 글을 읽고 공감가는 댓글을 30자 이내로 작성해줘"},
                {"role": "user", "content": f"블로그 글: {contnet}"}
            ]
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)

        try:
            content = response.json()["choices"][0]["message"]["content"]
            return content
        except KeyError:
            print("open_ai 응답 에러")