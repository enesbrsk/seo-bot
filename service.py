from utils import *
import time
import pyautogui

import webbrowser

def open_and_close_page(url, num_of_iterations):
    for _ in range(num_of_iterations):
        webbrowser.open(url)
        webbrowser.open("about:blank")
        time.sleep(10)
        pyautogui.hotkey('ctrl', 'w')
        change_ip()

def change_ip():
    ip_switch()
