import time  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Selenium 설정 (Chrome 드라이버)!
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 헤드리스 모드로 실행 (브라우저 창 없이 실행)

# 드라이버 경로 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 원하는 URL
url = "https://blog.naver.com/kook0923/223830922915"

# Selenium을 사용해 페이지 열기
driver.get(url)

# 페이지가 완전히 로드될 때까지 잠시 대기 (동적으로 로딩되는 콘텐츠가 있을 수 있기 때문에)
time.sleep(5)

# iframe으로 전환 (네이버 블로그는 본문이 iframe 안에 있음)
time.sleep(2)  # iframe 로딩 대기
driver.switch_to.frame("mainFrame")

# 본문 추출
try:
    content_element = driver.find_element(By.CSS_SELECTOR, "div.se-main-container")
    content_text = content_element.text
    print("본문 내용:\n", content_text[:1000])  # 1000자까지만 출력
    
    print("=====================================")
    # 텍스트를 공백 기준으로 나누어 단어 배열로 만들기
    words = content_text.split()

    # 100토큰만 출력
    tokens_to_print = words[:100]  # 처음 100개 단어만 추출

    # 100 토큰 출력
    print("100 토큰(단어):", " ".join(tokens_to_print))
except Exception as e:
    print("본문 추출 중 에러:", e)