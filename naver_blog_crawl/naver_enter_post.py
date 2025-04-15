import time
import pyperclip
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class EnterRecentPostBlog():
    def __init__(self):
        self.driver = None
    
    def open_web_mode(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.set_page_load_timeout(10)
            
    def enterPost(self):
        self.driver.get("https://section.blog.naver.com/")  # 네이버 블로그 메인 접속
        time.sleep(2)
        
        #
        for i in range(10):
            post_window = f"#content > section > div.list_post_article > div:nth-child({i+1}) > div.info_post > div.desc > a.desc_inner"
            
            post_window_element = self.driver.find_element(By.CSS_SELECTOR, post_window)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", post_window_element)
            time.sleep(1)
            post_window_element.click()
            time.sleep(5)
            
            # 클릭 등으로 새 탭이 열렸다고 가정
            tabs = self.driver.window_handles
            print("전체 탭 목록:", tabs)

            # 새로 생긴 탭으로 전환 (보통 마지막)
            self.driver.switch_to.window(tabs[-1])
            print("현재 탭 주소:", self.driver.current_url)
            
            # 새 탭 닫기
            self.driver.close()
            
            # 다시 기존 탭으로 돌아오기 (보통 첫 번째)
            self.driver.switch_to.window(tabs[0])

            time.sleep(1)
        
if __name__ == "__main__":
    try :
        enter_post_service = EnterRecentPostBlog()    
        enter_post_service.open_web_mode()
        enter_post_service.enterPost()
    except Exception as e:
        print("예외 발생:", e)
    finally:
        input("종료하려면 엔터를 누르세요.")
    