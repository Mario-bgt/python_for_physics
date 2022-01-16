from pynput.keyboard import Key, Controller
import time
from pathlib import Path

txt = Path('code.txt').read_text()
txt2 = Path('rank').read_text()
print(txt2)
keyboard = Controller()


def split(words):
    return [char for char in words]


time.sleep(4)
for i in split(txt):
    keyboard.type(i)
    time.sleep(0.05)