from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

class BasePage:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
            self.driver.implicitly_wait(5)

    def open(self, file_path):
        self.driver.get("file://" + os.path.abspath(file_path))
