#email generator


#imports
from operator import index
import select
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import random 
import names
import logging
import secrets
import string



logging.basicConfig(level=logging.INFO)


#getting the link and sleeping for 1 sec
driver = webdriver.Chrome()
url = "https://www.google.com/intl/en_uk/gmail/about/"
driver.get(url)
time.sleep(1)


#this part gets us to the account creation section
gmail_button = driver.find_element(By.XPATH, "/html/body/header/div/div/div/a[3]")
gmail_button.click()
time.sleep(2)


wait = WebDriverWait(driver, 10)


iterations = 1

#storing variables here 
random_first_name = names.get_first_name()
random_surname = names.get_last_name()

#Sorting the first name entry
for n in range(iterations):
    first_name_xpath = '//*[@id="firstName"]'
    first_name_input = driver.find_element(By.XPATH, first_name_xpath)
    first_name_input.send_keys(random_first_name)
    print(random_first_name)
    time.sleep(3)


#Sorting the surname
for s in range(iterations):
    surname_xpath = '//*[@id="lastName"]'
    surname_input = driver.find_element(By.XPATH, surname_xpath)
    surname_input.send_keys(random_surname)
    print(random_surname)
    time.sleep(2)


#pressing the 'next' button to proceed
next_button_xpath = '//*[@id="collectNameNext"]/div/button'
next_click = driver.find_element(By.XPATH, next_button_xpath)
next_click.click()
time.sleep(2)


#date of birth input 
for d in range(iterations):
    day_of_birth = random.randint(1,27)
    day_of_birth_xpath = '//*[@id="day"]'
    day_of_birth_input = driver.find_element(By.XPATH, day_of_birth_xpath)
    day_of_birth_input.send_keys(day_of_birth)
    time.sleep(2)


#year input
for y in range(iterations):
    year_of_birth = random.randint(1960,2000)
    year_of_birth_xpath = '//*[@id="year"]'
    year_of_birth_input = driver.find_element(By.XPATH, year_of_birth_xpath)
    year_of_birth_input.send_keys(str(year_of_birth))
    time.sleep(2)


#month input
month_dropbox_xpath = '//*[@id="month"]'
month_dropbox = driver.find_element(By.XPATH, month_dropbox_xpath)
select = Select(month_dropbox)
all_options = select.options
random_month_selection = random.choice(all_options)
select.select_by_visible_text(random_month_selection.text)
time.sleep(2)


#gender selection
gender_dropbox_xpath = '//*[@id="gender"]'
gender_dropbox = driver.find_element(By.XPATH, gender_dropbox_xpath)
select = Select(gender_dropbox)
options_to_choose_from = select.options
#make sure we dont press custom gender
options_to_choose_from = [option.text for option in select.options if option.text != "Custom"]
#gender selection with preferences 
random_gender_selection = random.choice(options_to_choose_from)
select.select_by_visible_text(random_gender_selection)
time.sleep(2)

#next button
birthdaygenderNext_button_xpath = '//*[@id="birthdaygenderNext"]/div/button'
next_click_2 = driver.find_element(By.XPATH, birthdaygenderNext_button_xpath)
next_click_2.click()
time.sleep(2)

#choose your gmail address
if driver.find_elements(By.XPATH, '//*[contains(@id, "selectionc")]'):
    choose_gmail_add_xpath = '//*[contains(@id, "selectionc")]'
    add_click = driver.find_element(By.XPATH, choose_gmail_add_xpath)
    selected_option_text = add_click.text
    add_click.click()
    print(selected_option_text)
    time.sleep(2)

else:
    email_address_entry = random_first_name + random_surname
    email_address_entry_xpath = '//*[@id="yDmH0d"]'
    email_address_entry = driver.find_element(By.XPATH, email_address_entry_xpath)
    email_address_entry.send_keys(email_address_entry)
    print(email_address_entry)
    time.sleep(2)
 
#next button x3
next_click_3_xpath = '//*[@id="next"]/div/button/span'
next_click_3 = driver.find_element(By.XPATH, next_click_3_xpath)
next_click_3.click()
time.sleep(3)

#password paths
password_xpath = '//*[@id="passwd"]/div[1]/div/div[1]/input'
confirm_password_xpath = '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input'

#password entry
password_entry = driver.find_element(By.XPATH, password_xpath)
confirm_password_entry = driver.find_element(By.XPATH, confirm_password_xpath)
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))
password_entry.send_keys(password)
confirm_password_entry.send_keys(password)
print(password)
time.sleep(2)

#next_button4
next_click_4_xpath = '//*[@id="createpasswordNext"]/div/button/span'
next_click_4 = driver.find_element(By.XPATH, next_click_4_xpath)
next_click_4.click()
time.sleep(2)

#phone number entry
#phone_number_entry_xpath = '//*[@id="phoneNumberId"]'



