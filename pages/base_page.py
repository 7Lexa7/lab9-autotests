from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

class BasePage:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            # Используем системный ChromeDriver в GitHub Actions
            chrome_driver_path = os.path.join(os.environ.get('CHROMEWEBDRIVER', '/usr/local/bin'), 'chromedriver')
            service = Service(executable_path=chrome_driver_path)
            
            # Настройки для запуска в CI (без графического интерфейса)
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.implicitly_wait(5)

    def open(self, file_path):
        # Для локального запуска используем file:// протокол
        full_path = os.path.abspath(file_path)
        # Убедимся, что путь правильный для разных ОС
        if os.name == 'nt':  # Windows
            file_url = f"file:///{full_path.replace('\\', '/')}"
        else:  # Linux/macOS
            file_url = f"file://{full_path}"
        
        self.driver.get(file_url)