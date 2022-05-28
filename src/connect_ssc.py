import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

cwl = 'cwl'
password = 'password'

courses = []

chromedriver = Service('C:\\Users\ofekz\Python\CourseScheduler\chromedriver_win32\chromedriver.exe')
chrome = webdriver.Chrome(service=chromedriver, options=webdriver.ChromeOptions())
chrome.get('https://cas.id.ubc.ca/ubc-cas/login?TARGET=https%3A%2F%2Fssc.adm.ubc.ca%2Fsscportal%2Fservlets%2FSRVSSCFramework')

class SSCConnector:

    def __init__(self):
        pass

    def login():
        pass

    def create_worklist():
        pass

    def add_courses():
        pass
