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

class NaverLoginService():
    def __init__(self):
        self.driver = None
        
    def open_web_mode(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.set_page_load_timeout(10)
    
    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
    
    def login(self):
        self.driver.get("https://nid.naver.com/nidlogin.login")
        time.sleep(2)
        
        test_id = "seo970713"
        test_passwd = "gjspark975!!"
        
        id_input = self.driver.find_element(By.ID, "id")
        id_input.click()
        pyperclip.copy(test_id)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        
        pw_input = self.driver.find_element(By.ID, "pw")
        pw_input.click()
        pyperclip.copy(test_passwd)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        
        self.driver.find_element(By.ID, "log.login").click()
        
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.btn_cancel"))
            )
            element.click()
        except:
            print("기기 등록 '등록안함' 버튼을 찾을 수 없습니다.")
            
    def comment(self):
        # 네이버 블로그 게시글 URL (댓글 달 대상)
        blog_post_url = "https://blog.naver.com/kook0923/223830922915"

        # 해당 URL 접속
        self.driver.get(blog_post_url)
        time.sleep(5)   # 로딩 대기

        # iframe으로 되어있으므로 전환 필요
        self.driver.switch_to.frame("mainFrame")
        time.sleep(1)

        # 댓글 창까지 스크롤 및 댓글 버튼 클릭 (댓글 창 열기)
        comment = "#printPost1 > tbody > tr > td.bcc > div.post-btn.post_btn2 > div.wrap_postcomment > div.area_comment.pcol2"
        comment_element = self.driver.find_element(By.CSS_SELECTOR, comment)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", comment_element)
        comment_element.click()
        time.sleep(1)
        
        # 댓글 리스트 스크롤 및 댓글 박스 클릭
        comment_window = "#naverComment_201_223830922915 > div > div.u_cbox_write_wrap > div.u_cbox_write_box.u_cbox_type_logged_in > form > fieldset > div > div > div.u_cbox_write_area > div"
        comment_window_element = self.driver.find_element(By.CSS_SELECTOR, comment_window)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", comment_window_element)
        comment_window_element.click()
        
        #
        pyperclip.copy("안녕하세요! 좋은 글 감사합니다. :)")
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", comment_window_element)
        time.sleep(1)
        
        # 비밀댓글 버튼 클릭
        secret_comment = "#naverComment_201_223830922915 > div > div.u_cbox_write_wrap.u_cbox_writing > div.u_cbox_write_box.u_cbox_type_logged_in > form > fieldset > div > div > div.u_cbox_upload > div > span.u_cbox_secret_tag"
        btn_secret_comment = self.driver.find_element(By.CSS_SELECTOR, secret_comment)
        btn_secret_comment.click()
        time.sleep(1)
        
        # 등록버튼 버튼 클릭
        register_window = "#naverComment_201_223830922915 > div > div.u_cbox_write_wrap.u_cbox_writing > div.u_cbox_write_box.u_cbox_type_logged_in > form > fieldset > div > div > div.u_cbox_upload > button > span.u_cbox_txt_upload"
        register_element = self.driver.find_element(By.CSS_SELECTOR, register_window)
        register_element.click()
    
        
        # comment_area.send_keys("안녕하세요! 좋은 글 감사합니다. :)")
            
if __name__ == "__main__":
    try:
        naver_service = NaverLoginService()
        naver_service.open_web_mode()
        naver_service.login()
        time.sleep(1)
        naver_service.comment()
        # naver_service.close_browser()
    except Exception as e:
        print("예외 발생:", e)
    finally:
        input("종료하려면 엔터를 누르세요.")
    
        
        
