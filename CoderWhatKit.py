import webbrowser
import time
from urllib.parse import quote_plus
import pyautogui
import datetime
import re

def send_message(PHONE_NUMBER, MESSAGE: str):
    encoded_message = quote_plus(MESSAGE)    
    url = f"https://web.whatsapp.com/send?phone={PHONE_NUMBER}&text={encoded_message}"
    webbrowser.open(url)
    time.sleep(5)
    pyautogui.press('enter')
    saat = datetime.datetime.now().strftime("%H:%M")
    NEW_NUMBER = re.sub(r'^Enter the country phone code', '', PHONE_NUMBER)

    Log = f"Number: {NEW_NUMBER}\nMessage: {MESSAGE}\nTime: {saat}\n----------------------------\n"

    with open("CoderWhatKit_Log.txt", "a", encoding="utf-8") as file:
        file.write(Log)