from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)
        self.name_input = (By.ID, "name")
        self.email_input = (By.ID, "email")
        self.message_input = (By.ID, "message")
        self.submit_button = (By.ID, "submitBtn")
        self.success_msg = (By.ID, "successMsg")
        self.error_msg = (By.ID, "errorMsg")

    def fill_form(self, name="", email="", message=""):
        self.driver.find_element(*self.name_input).clear()
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.email_input).clear()
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.message_input).clear()
        self.driver.find_element(*self.message_input).send_keys(message)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_msg).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).is_displayed()
