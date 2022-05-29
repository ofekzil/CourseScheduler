import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys
import time

assert len(sys.argv) == 3

cwl = str(sys.argv[1])
password = str(sys.argv[2])

courses = []


class SSCConnector:

    def __init__(self):
        chromedriver = Service('C:\\Users\ofekz\Python\CourseScheduler\chromedriver_win32\chromedriver.exe')
        self.browser = webdriver.Chrome(service=chromedriver, options=webdriver.ChromeOptions())

    # log into course schedule page in ssc
    def login(self):
        self.browser.execute_script('''window.open("https://cas.id.ubc.ca/ubc-cas/login?TARGET=https%3A%2F%2Fssc.adm.ubc.ca%2Fsscportal%2Fservlets%2FSRVSSCFramework","_blank");''')
        self.browser.switch_to.window(self.browser.window_handles[-1])
        username_field = self.browser.find_element(By.NAME,'username')
        pw_field = self.browser.find_element(By.NAME, 'password')
        username_field.clear()
        username_field.send_keys(cwl)
        print(cwl)
        pw_field.clear()
        pw_field.send_keys(password)
        print(password)
        self.browser.find_element(By.NAME, 'submit').click()
        time.sleep(10)

    # selects appropriate session
    def select_session(self,session):
        # print(self.browser.window_handles)
        # print(self.browser.current_window_handle)
        pass

    # creates a worklist
    def create_worklist(self):
        pass

    # adds given courses to worklist that was created
    def add_courses(self):
        pass

connector = SSCConnector()

connector.login()
connector.select_session('2022 Winter')