from common import *
from naver_login import NaverLogin
from naver_blog_service import NaverBlogService

class Main:
    def __init__(self):
        self.driver = None
        
    def open_web_mode(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.set_page_load_timeout(10)
        
    def close_browser(self):
        if self.driver:
            self.driver.quit(self.driver)
            self.driver = None
    
    def login(self):
        login = NaverLogin(self.driver)
        login.login()
        
    def service(self):
        service = NaverBlogService(self.driver)
        service.service()
        
if __name__ == "__main__":
    try:
        main = Main()
        main.open_web_mode()
        main.login()
        main.service()
        
    except Exception as e:
        print("예외 발생:", e)
    finally:
        input("종료하려면 엔터를 누르세요.")