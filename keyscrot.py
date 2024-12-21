import pyautogui
import os
from pynput import keyboard
from datetime import datetime

screenshot_dir = os.path.expanduser("~/screen")
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

screenshot_counters = {}

def take_screenshot():
    current_year = datetime.now().year
    if current_year not in screenshot_counters:
        screenshot_counters[current_year] = 1
    else:
        screenshot_counters[current_year] += 1
    screenshot_path = os.path.join(screenshot_dir, f"screen{current_year}_{screenshot_counters[current_year]:04d}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)

def on_press(key):
    if key == keyboard.Key.end:
        return False
    elif key == keyboard.Key.scroll_lock:
        take_screenshot()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
