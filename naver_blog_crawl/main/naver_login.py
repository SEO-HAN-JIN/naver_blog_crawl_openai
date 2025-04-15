from common import *
import config

class NaverLogin:
    def __init__(self, driver):
        self.driver = driver
        
    def login(self):
        self.driver.get("https://nid.naver.com/nidlogin.login")
        time.sleep(2)
        
        test_id = config.USERNAME
        test_passwd = config.PASSWORD
        
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