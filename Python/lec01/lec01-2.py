# this is a source code
import pyautogui

# run some program
pyautogui.hotkey('win','r')

# mspaint
pyautogui.typewrite('mspaint')
pyautogui.press('enter')

# wait for a while
pyautogui.moveRel(1,1,1)

# maximize the window
pyautogui.hotkey('win','up')

# 選三角形
pyautogui.moveTo(499, 65, 0.5)
pyautogui.click()

# 選填滿
pyautogui.click(560,83)
pyautogui.moveTo(551,136,0.5)
pyautogui.click()

# 選顏色
pyautogui.click(691,69)
pyautogui.click(897,82)
pyautogui.click(733,69)
pyautogui.click(897,82)

# 畫三角形
pyautogui.moveTo(307,200)
pyautogui.dragRel(100,100,0.1)





