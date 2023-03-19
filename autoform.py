import pyautogui
import time
def Click(x,y):
	pyautogui.click(x,y)
	pyautogui.click()

def GoAndType(x,y,text):
	Click(x,y)
	time.sleep(1)
	pyautogui.write(text)

def Autoform(food,other):
	GoAndType(1198,397,food)
	GoAndType(1182,567,other)
	Click(1166,653)

Autoform('Kaokaijiao','KungSod')
