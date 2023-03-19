import webbrowser
import time
import pyperclip
import pyautogui as pg
from datetime import datetime
##########1##########
# เปิดเว็บบราวเซอร์
# -ใช้ library อะไร? > import webbrowser
# -function ไหน? > .open(url)

##########2##########
# เปิด Google
# -ใช้ library อะไร? > webbrowser
# -function ไหน? > .open(url)
# -เว็บอะไร? > https://www.google.com

url = 'https://www.google.com'

webbrowser.open_new(url)
time.sleep(2)
##########3##########
# พิมพ์คำสั่งที่ต้องการ เช็คสภาพอากาศ
# -ใช้ library อะไร? > pyautogui
# -function ไหน? > .write() / pyperclip.copy(), .hotkey() สำหรับภาษาไทย
# -keyword อะไร? > "สภาพอากาศพญาไท กรุงเทพ", "สภาพอากาศภูชี้ฟ้า"

keyword = 'สภาพอากาศเชียงใหม่'
pyperclip.copy(keyword)
time.sleep(1)
pg.hotkey('ctrl','v')
time.sleep(1)
pg.press('enter')
time.sleep(2)

##########4##########
# แคปเจอร์สกรีนผลลัพธ์
# -ใช้ library อะไร? > pyautogui
# -function ไหน? > .screenshot('test.jpg')
position = (144,410,1031,548)

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M') #strftime.org

filename = '{}-{}.jpg'.format(timestamp,keyword)
pg.screenshot(filename, region=position)