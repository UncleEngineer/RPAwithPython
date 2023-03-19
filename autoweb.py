# username: loongcar@gmail.com
# password: 123456

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

options = webdriver.ChromeOptions()
# options.add_argument('--start-maximized')
#options.add_argument('window-size=1920,1080')
#options.add_argument('headless') #ไม่ต้องเปิดบราวเซอร์

path = r'C:\Users\Uncle Engineer\Desktop\RPA with Python\chromedriver.exe'
ser =  Service(path)

driver = webdriver.Chrome(service=ser)
url = 'http://uncle-machine.com/login/'
driver.get(url)
time.sleep(2)

username_text = 'loongcar@gmail.com'
password_text = '123456'

username = driver.find_element(By.ID,'username')
username.send_keys(username_text)

password = driver.find_element(By.ID,'password')
password.send_keys(password_text)

button_path = '/html/body/div[2]/form/button'

button = driver.find_element(By.XPATH, button_path)
button.click()
time.sleep(2)

###############Next Page###############
import wikipedia
wikipedia.set_lang('th')

keyword = ['องุ่น','ส้มโชกุน','ทุเรียน']

for k in keyword:
    url2 = 'http://uncle-machine.com/addproduct/'
    driver.get(url2)
    time.sleep(2)
    try:
        wikidetail = wikipedia.summary(k)
        product_name = driver.find_element(By.ID,'name')
        product_name.send_keys(k)
        price = driver.find_element(By.ID,'price')
        price.send_keys('20000')
        detail = driver.find_element(By.ID,'detail')
        detail.send_keys(wikidetail)

        if k == 'ทุเรียน':
            filepath = r'C:\Users\Uncle Engineer\Desktop\RPA with Python\durian.jpg'
            photo = driver.find_element(By.ID,'photo')
            photo.send_keys(filepath) #ใส่ตำแหน่งของภาพ


        b2_path = '/html/body/div[2]/form/button'
        button = driver.find_element(By.XPATH, b2_path)
        button.click()
        time.sleep(1)

        
    except:
        print('Keyword Error: ',k)
        pass

wait = input('waiting...')
driver.quit()