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
    special_div = soup.find('div', class_="word active")
    divs = soup.find_all('div', class_="word")
    text = ""

    for div in special_div:
        nested_divs = div.find_all('letter')
        for i in nested_divs:
            if 'letter' in str(i):
                text += i.text
        text += " "

    for div in divs:
        nested_divs = div.find_all('letter')
        for i in nested_divs:
            if 'letter' in str(i):
                text += i.text
        text += " "
    

    if not text:
        print("no text was found")
        return None
    else:
        print("this is the text: ", text)
    return text

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get('https://monkeytype.com/')

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
