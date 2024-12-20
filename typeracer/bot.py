from bs4 import BeautifulSoup
from pynput.keyboard import Controller
from pynput import keyboard
import time
from selenium import webdriver

keyb = Controller()

def get_text_to_type(driver):

    time.sleep(1)
    scr = driver.page_source
    soup = BeautifulSoup(scr, 'html.parser')
    span = soup.find_all('span')
    text = ""

    for i in span:
        if 'unselectable' in str(i):
            text += i.text
    
    if not text:
        print("no text was found")
        return None
    else:
        print("this is the text: ", text)
    return text

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get('https://play.typeracer.com/')

def main():

    text_to_type = get_text_to_type(driver)
    if text_to_type:
        for c in text_to_type:
            keyb.press(c)
            keyb.release(c)
            time.sleep(0.05)


def on_activate():
    main()

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+h'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press)) as l:
    l.join()
