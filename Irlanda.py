import psutil
import time
from colorama import Fore
import CoderWhatKit
import sys
import pyautogui

blocked_apps = ["Discord.exe", "TLauncher.exe"]
print("-----------------------------------------")

PASSWORD = "Monch-231!"

def main():
    time.sleep(1)
    while True:
        for proc in psutil.process_iter(['pid','name']):
            name = proc.info['name']
            pid = proc.info['pid']

            if name in blocked_apps:
                proc.kill()
                print(Fore.RED + f"Kapandı: {name}:{pid}")
                sor = input("Şifreyi gir: ")
                if sor != PASSWORD:
                    CoderWhatKit.send_message("Write Your Phone Number", "Write Message")
                    time.sleep(6)
                    pyautogui.press('enter')
                else:
                    sys.exit(0)
                return main()
            else:
                continue

main()