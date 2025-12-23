import pytest
import time
from pages.contact_page import ContactPage

def test_contact_form_positive():
    page = ContactPage()
    page.open("contact_form.html")
    page.fill_form(name="Иван", email="ivan@mail.com", message="Привет!")
    page.submit_form()
    
 
    time.sleep(3)

    assert page.get_success_message() == True
    time.sleep(3) 
