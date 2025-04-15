import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# 크롬 드라이버 경로 지정
driver = webdriver.Chrome()

# 네이버 로그인 페이지로 이동
driver.get("https://nid.naver.com/nidlogin.login")

# 로그인 정보 입력
username = driver.find_element(By.ID, "id")
password = driver.find_element(By.ID, "pw")

for char in "seo970713":
    username.send_keys(char)
    time.sleep(0.5)

for char in "gjspark975!!":
    password.send_keys(char)
    time.sleep(0.5)
# username.send_keys("seo970713")  # 네이버 아이디 입력
# password.send_keys("gjspark975!!")  # 네이버 비밀번호 입력
time.sleep(5)
password.send_keys(Keys.RETURN)  # 로그인 버튼 클릭
time.sleep(5)




# 네이버 블로그 게시글 URL (댓글 달 대상)
blog_post_url = "https://blog.naver.com/kook0923/223830922915"

# 해당 URL 접속
driver.get(blog_post_url)
time.sleep(5)   # 로딩 대기

# iframe으로 되어있으므로 전환 필요
driver.switch_to.frame("mainFrame")
time.sleep(1)

# 댓글 창 열기
driver.execute_script("document.getElementById('naverComment_201_223830922915_ct').style.display='block';")

# 댓글 입력 영역 찾기 (셀렉터는 글에 따라 다를 수 있음)
comment_area = driver.find_element(By.CSS_SELECTOR, "textarea.u_cbox_text")
comment_area.send_keys("안녕하세요! 좋은 글 감사합니다. :)")

time.sleep(1)