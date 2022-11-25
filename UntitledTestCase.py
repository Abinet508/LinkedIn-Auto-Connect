#! python
from csv import excel_tab
import email
from selectors import SelectSelector
from sqlite3 import connect

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from decouple import AutoConfig
class LinkedIn(unittest.TestCase):
    def setUp(self):
        options = Options()
        #options.add_argument('--headless')
        #options.add_argument('--disable-gpu') 
        self.driver = webdriver.Chrome(options=options)
        self.driver.headless=True
        self.driver.implicitly_wait(300)
        self.driver.set_page_load_timeout(300)
        self.driver.maximize_window()
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        config = AutoConfig('Credential/.env')
        email=config('EMAIL')
        password=config('PASSWORD')
        profession=config('PROFILE').capitalize()
        country=config('COUNTERY').capitalize()
        driver = self.driver
        driver.get("https://www.linkedin.com/login")
        driver.set_page_load_timeout(300)
        
        driver.find_element(By.ID,"username").clear()
        driver.find_element(By.ID,"username").send_keys(email)
        time.sleep(2)
        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys(password)
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(2)
        if profession =="":
            RecommendedNetwork = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[@title='My Network']")))
            RecommendedNetwork.click()
        else:
            Filters = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Search']")))
            Filters.click()
            Filters.clear()
            Filters.send_keys(profession)
            Filters.send_keys(Keys.ENTER)
            #driver.find_element(By.XPATH,"//input[@data-job-search-box-keywords-input-trigger='{}']").send_keys()
           #pyautogui.press("enter")
            time.sleep(2)
            People = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='People']")))
            People.click()
            time.sleep(2)
            Locations=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Locations']")))
            Locations.click()
            Add_location=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='United States']")))
            Add_location.click()
            
            time.sleep(2)
            Show_results=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//span[text()='Show results'])[2]")))
            Show_results.click()
        time.sleep(5)
        #element2 = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//ul/li[3]//ul/li")))
        html = driver.find_element(By.TAG_NAME,'html')
        for row in range(0,80):
            
            try:
                print("connect")
                driver.implicitly_wait(6)
                Connect=Connect=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Connect']")))  
                Connect.click()
                time.sleep(2)
                print(profession)
                if not (profession ==""):
                    try:
                        driver.implicitly_wait(10)
                        Send=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send now']")))
                        Send.click()
                    except:    
                        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send now']"))))

                   
                
            except Exception as e:
                #print(e)
                if not(profession ==""):
                    try:
                        driver.implicitly_wait(10)
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  
                        time.sleep(2)
                        print('clicking Next')
                        next= driver.find_element(By.XPATH,"//span[text()='Next']/parent::*")
                        actions = ActionChains(driver)
                        actions.move_to_element(next).perform()
                        next.click()
                    except:
                        driver.implicitly_wait(10)
                        html.send_keys(Keys.PAGE_DOWN)
                        time.sleep(2)
                        driver.switch_to.window(driver.window_handles[0])
                        if driver.find_element(By.XPATH,"//h2[@id='ip-fuse-limit-alert__header']").text=="You’ve reached the weekly invitation limit":
                            print("You’ve reached the weekly invitation limit")
                        
                        driver.quit()
                        driver.find_element(By.XPATH,"//span[text()='Got it']").click() 
            finally:
                time.sleep(2)
                driver.implicitly_wait(6)
                Connect=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Connect']")))  
                try:
                    Connect.click()
                except:
                        driver.execute_script("arguments[0].click();", Connect) 
                finally:
                    print(profession)
                    if not (profession ==""):
                        try:
                            driver.implicitly_wait(10)
                            Send=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send now']")))
                            Send.click()
                        except:    
                            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send now']"))))
   
                                    
                time.sleep(2)
                
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
