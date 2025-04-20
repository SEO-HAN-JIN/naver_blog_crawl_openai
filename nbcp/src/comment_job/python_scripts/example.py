import requests
import time

def send_post(index):
    url = "http://host.docker.internal:8080/api/comment-logs"
    data = {
        "userId": f"auto_bot_{index}",
        "blogUrl": f"http://myblog.com/post/{index}",
        "comment": f"[{index}] 자동 주고 전송 테스트입니다."
    }

    response = requests.post(url, json=data)
    print(f"응답 코드: {response.status_code}, 응답 내용: {response.text}")

for i in range(10):
    print(f"{i+1}번째 요청 중...")
    send_post(i)  # <- 여기 수정!
    if i < 9:
        time.sleep(20)
