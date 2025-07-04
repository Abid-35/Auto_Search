import pyautogui

profile=0

getthedata=[]
pyautogui.PAUSE=1.8
pyautogui.press('win')
pyautogui.write('ed',interval=0.1)
pyautogui.press('enter')


s=['nenuloacal','hydrebad','flight','usa','culters in india','sea food','varocious','gram','keledio','solar']
ser=['ganesh','nava','yaswanth','vamsi','lokesh','shalem','vishnu','sriram','nani','aarif','tarun','varun','laxmu','nagaraju','tanvish','sai','babi','vivek','kiran','charan']
getthedata=s+ser

for i in getthedata:
     pyautogui.write(i,interval=0.1)
     pyautogui.press('enter')
     pyautogui.doubleClick(397,147)#149,166
     pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('alt','f4')