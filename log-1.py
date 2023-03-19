Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyautogui
>>> pyautogui.moveTo(50,50)
>>> pyautogui.moveTo(-50,50)
>>> pyautogui.moveTo(-100,50)
>>> pyautogui.moveTo(-1000,50)
>>> pyautogui.moveTo(50,50,5)
>>> pyautogui.moveTo(50,50,5)
>>> menu = 'Kaomankai'
>>> print(menu)
Kaomankai
>>> pyautogui.position()
Point(x=851, y=409)
>>> pyautogui.position()
Point(x=842, y=609)
>>> def Hello():
	print('hello my friend')
	print('how are you?')

	
>>> Hello()
hello my friend
how are you?
>>> Hello()
hello my friend
how are you?
>>> Hello()
hello my friend
how are you?
>>> def Sawatdee(friend):
	print('สวัสดี'+friend)
	print('สบายดีไหม?')

	
>>> Sawatdee('จ้อย')
สวัสดีจ้อย
สบายดีไหม?
>>> Sawatdee('John')
สวัสดีJohn
สบายดีไหม?
>>> import pyautogui
>>> import time
>>> def Click(x,y):
	pyautogui.click(x,y)
	pyautogui.click()

	
>>> Click(851,409)
>>> Click(851,609)
>>> def GoAndType(x,y,text):
	Click(x,y)
	time.sleep(1)
	pyautogui.write(text)

	
>>> GoAndType(851,409,'Kaomankai')
>>> GoAndType(851,609,'Mainung')
>>> pyautogui.position()
Point(x=833, y=694)
>>> pyautogui.position()
Point(x=839, y=658)
>>> Click(839,694)
>>> Click(839,658)
>>> def Autoform(food,other):
	GoAndType(851,409,food)
	GoAndType(851,609,other)
	Click(839,658)

	
>>> pyautogui.click(839,658)
>>> pyautogui.click(839,658)
>>> pyautogui.click(839,658)
>>> pyautogui.moveTo(839,658)
>>> pyautogui.moveTo(839,658)
>>> pyautogui.moveTo(851,409)
>>> pyautogui.moveTo(851,609)
>>> pyautogui.moveTo(851,409)
>>> pyautogui.moveTo(851,609)
>>> pyautogui.moveTo(851,609)
>>> Autoform('Kaokaijiao','KungSod')
>>> Autoform('Kaokaijiao','KungSod')
>>> Autoform('Kaokaijiao','KungSod')
>>> pyautogui.position()
Point(x=841, y=439)
>>> pyautogui.position()
Point(x=842, y=604)
>>> pyautogui.position()
Point(x=849, y=686)
>>> def Autoform(food,other):
	GoAndType(851,409,food)
	GoAndType(851,609,other)
	Click(839,658)

	
>>> def Autoform(food,other):
	GoAndType(841,439,food)
	GoAndType(842,604,other)
	Click(849,686)

	
>>> Autoform('Kaokaijiao','KungSod')
>>> Autoform('Kaopadpu','Prikthai yeue yeue')
>>> 