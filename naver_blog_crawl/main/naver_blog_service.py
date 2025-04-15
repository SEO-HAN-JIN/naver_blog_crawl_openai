from common import *
from openai_api import OpenAiIntegration

class NaverBlogService:
    def __init__(self, driver):
        self.driver = driver
        
    def enterPost(self):
        self.driver.get("https://section.blog.naver.com/")  # 네이버 블로그 메인 접속
        time.sleep(2)
        
        #
        for i in range(3):
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
            post_url = self.driver.current_url
            post_id = post_url.split("/")[-1]
            print("현재 탭 주소:", post_url)
            
            # 본문 스크랩
            content_text = self.scrapMainContent()
            
            # open_ai 호출
            openai = OpenAiIntegration()  # OpenAI 객체 생성
            comment = openai.send_to_openai(content_text)
            print("AI 댓글:", comment)
            
            self.scrollComment(post_id, comment)
            
            # 새 탭 닫기
            self.driver.close()
            
            # 다시 기존 탭으로 돌아오기 (보통 첫 번째)
            self.driver.switch_to.window(tabs[0])

            time.sleep(1)
            
    def scrapMainContent(self):
        
        # iframe으로 되어있으므로 전환 필요
        self.driver.switch_to.frame("mainFrame")
        time.sleep(1)
        
        content_element = self.driver.find_element(By.CSS_SELECTOR, "div.se-main-container")
        content_text = content_element.text
        return content_text
            
    def scrollComment(self, post_id, comment_text):

        # 댓글 창까지 스크롤 및 댓글 버튼 클릭 (댓글 창 열기)
        comment = "#printPost1 > tbody > tr > td.bcc > div.post-btn.post_btn2 > div.wrap_postcomment > div.area_comment.pcol2"
        comment_element = self.driver.find_element(By.CSS_SELECTOR, comment)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", comment_element)
        comment_element.click()
        time.sleep(1)
        
        # 댓글 리스트 스크롤 및 댓글 박스 클릭
        comment_window = f"#naverComment_201_{post_id} > div > div.u_cbox_write_wrap > div.u_cbox_write_box.u_cbox_type_logged_in > form > fieldset > div > div > div.u_cbox_write_area > div"
        comment_window_element = self.driver.find_element(By.CSS_SELECTOR, comment_window)
        self.driver.execute_script("arguments[0].scrollIntoView(false);", comment_window_element)
        comment_window_element.click()
        
        #
        pyperclip.copy(comment_text)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(1)
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", comment_window_element)
        time.sleep(1)
        
        # 비밀댓글 버튼 클릭
        secret_comment = f"#naverComment_201_{post_id} > div > div.u_cbox_write_wrap.u_cbox_writing > div.u_cbox_write_box.u_cbox_type_logged_in > form > fieldset > div > div > div.u_cbox_upload > div > span.u_cbox_secret_tag"
        btn_secret_comment = self.driver.find_element(By.CSS_SELECTOR, secret_comment)
        btn_secret_comment.click()
        time.sleep(1)
        
        # 등록버튼 버튼 클릭
        register_window = f"#naverComment_201_{post_id} > div > div.u_cbox_write_wrap.u_cbox_writing > div.u_cbox_write_box.u_cbox_type_logged_in > form > fieldset > div > div > div.u_cbox_upload > button > span.u_cbox_txt_upload"
        register_element = self.driver.find_element(By.CSS_SELECTOR, register_window)
        register_element.click()
        time.sleep(3)
        
    def service(self):
        self.enterPost()
        # self.scrollComment()