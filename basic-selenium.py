from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

options = webdriver.ChromeOptions()
# options.add_argument('--start-maximized')
options.add_argument('window-size=1920,1080')
options.add_argument('headless') #ไม่ต้องเปิดบราวเซอร์

path = r'C:\Users\Uncle Engineer\Desktop\RPA with Python\chromedriver.exe'
ser =  Service(path)

driver = webdriver.Chrome(service=ser,options=options)
url = 'https://www.google.com'
##############################
keyword = ['อุณหภูมิ กรุงเทพ','อุณหภูมิ เชียงใหม่','อุณหภูมิ ภูเก็ต']

for k in keyword:
    #open web
    driver.get(url)
    # find  element
    search = driver.find_element(By.NAME,'q')
    search.send_keys(k)
    #ส่งปุ่ม enter เข้าไปเพื่อให้เริ่มค้นหา
    search.send_keys(Keys.RETURN)
    time.sleep(1)
    #save screenshot
    t = datetime.now().strftime('%Y-%m-%d %H%M%S')
    driver.save_screenshot('{}-{}.png'.format(t,k))

##############################
#wait = input('Waiting...')
#time.sleep(10)
driver.close() 