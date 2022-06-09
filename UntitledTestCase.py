#! python
from csv import excel_tab
import email
from selectors import SelectSelector
from sqlite3 import connect
from typing_extensions import Self
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
        options.add_argument('--headless')
        options.add_argument('--disable-gpu') 
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
        driver = self.driver
        driver.get("https://www.linkedin.com/login")
        driver.set_page_load_timeout(300)
        driver.implicitly_wait(300)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(email)
        time.sleep(2)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        time.sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//li/a[@data-control-name='nav_mynetwork']")))
        element.click()
        time.sleep(15)
        #element2 = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//ul/li[3]//ul/li")))
        html = driver.find_element_by_tag_name('html')
        for row in range(0,80):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Connect']")))
                connect= driver.find_element_by_xpath("//button/span[text()='Connect']")
                actions = ActionChains(driver)
                actions.move_to_element(connect).perform()
            except:
                print("No connect button")
                driver.switch_to.window(driver.window_handles[0])
                if driver.find_element_by_xpath("//h2[@id='ip-fuse-limit-alert__header']").text=="You’ve reached the weekly invitation limit":
                   print("You’ve reached the weekly invitation limit")
                   
                   driver.quit()
                driver.find_element_by_xpath("//span[text()='Got it']").click() 
            finally:    
                try:
                    connect.click()
                except:
                        driver.execute_script("arguments[0].click();", connect) 
                   
                                    
                time.sleep(2)
                
                html.send_keys(Keys.PAGE_DOWN)
                time.sleep(2)
                #element2 = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//ul/li[3]//ul/li")))
            
                #length = len(list(driver.find_elements_by_xpath("//ul/li[3]//ul/li")))
                #print(length)
            #ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=//aside[@id='msg-overlay']/div/header/div | ]]
        
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
