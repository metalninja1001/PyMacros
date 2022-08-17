#import modules
import time
import pyautogui

#set delay between when the script is executed until the mouse location is recorded.
time.sleep(10)
#print mouse location with x and y coordinates.
print(pyautogui.position())
