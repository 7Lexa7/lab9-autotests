import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.contact_page import ContactPage

def test_contact_form_negative():
    # Инициализация драйвера для GitHub Actions
    chrome_driver_path = os.path.join(os.environ.get('CHROMEWEBDRIVER', '/usr/local/bin'), 'chromedriver')
    service = Service(executable_path=chrome_driver_path)
    
    options = Options()
    options.add_argument('--headless')  # Запуск без графического интерфейса
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        page = ContactPage(driver)
        page.open("contact_form.html")
        
        page.fill_form(name="", email="ivan@mail.com", message="Привет!")
        page.submit_form()
        
        time.sleep(3)
        
        assert page.get_error_message() == True
        
    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])