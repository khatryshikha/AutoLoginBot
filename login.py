import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def job():
    usernameStr = 'shikha_514'
    passwordStr = 'You@1234'

    driver = webdriver.Chrome(executable_path='/home/shikha/chromedriver')
    driver.get(('http://172.22.252.11/login'))

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username")))
    username.send_keys(usernameStr)

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password")))
    password.send_keys(passwordStr)

    signInButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/form/table/tbody/tr[3]/td[2]/input")))
    signInButton.click()
    driver.quit()

schedule.every().day.at("00:00").do(job)
schedule.every().day.at("08:00").do(job)
schedule.every().day.at("16:00").do(job)

while True:
    schedule.run_all()
    time.sleep(60)