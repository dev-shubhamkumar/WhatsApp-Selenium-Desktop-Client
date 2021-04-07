from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
import time
import win32com.client


# #-----------------------------------------------------------------------
# from whatsapp.whatsapp_client import WhatsappWebController

PATH = r'C:\Users\devsh\Desktop\whatsapp_bot_client\driver\chromedriver_win32\chromedriver.exe'

# wp = WhatsappWebController(PATH)
# wp.open_whatsapp_web(sleep_time=30)


# contact_name = 'Pratyush Nishantkar'

# error_status, chat_list = wp.read_entire_chat(contact_name)


# #------------------------------------------------------------------------


user_name = 'Pratyush Nishantkar'


driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")

time.sleep(30)
print('\n\nThe test is.....\n\n')
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()

print('\n\nPlease Manipulate.....\n\n')
time.sleep(30)
images = driver.find_elements_by_partial_link_text('blob:https://web.whatsapp.com/')

for img in images:
    print('\n\n{}\n\n'.format(img.text))







