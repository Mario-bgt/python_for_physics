import pyautogui
import webbrowser
import time

message = input("Mario is great ")
repeats = 20
delay = 200

isLoaded = input("Press Enter when your messaging app is loaded up.")



print("You have five seconds to refocus the text input area of your messaging app")

time.sleep(5)


for i in range(0,repeats):         #Message sending loop
	if message != "":
		pyautogui.typewrite(message)
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.press("enter")

	time.sleep(delay/1000)


print("Done\n")