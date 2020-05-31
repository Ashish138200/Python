import pyautogui
pyautogui.screenshot('ss.png')
pyautogui.locateOnScreen('Image Location') #slow and pixel perfect
pyautogui.locateCenterOnScreen('Image Location')
pyautogui.moveTo((coordinates),duration=1)
pyautogui.click(coordinates)