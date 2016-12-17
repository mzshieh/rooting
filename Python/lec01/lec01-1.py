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
