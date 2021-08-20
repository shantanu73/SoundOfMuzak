from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# usr = input('Enter Email Id:')
# pwd = input('Enter Password:')

email_id = "shantanudhiman25"
password = "dhimanshantanu"
recovery_email_id = "shantanudhiman73@gmail.com"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://docs.google.com/document/u/0/')
input_email = driver.find_element_by_xpath("//input[@type='email']")
if input_email:
    input_email.send_keys(email_id)
    next_button = driver.find_element_by_xpath("//button[@type='button']")
    next_button.click()
sleep(1)
recovery = driver.find_element_by_xpath("//input[@type='email'][@aria-label='Phone number or email']")
if recovery:
    recovery.send_keys(recovery_email_id)
    next_button = driver.find_element_by_xpath("//button[@type='button']")
    next_button.click()

print("Opened Google docs")
