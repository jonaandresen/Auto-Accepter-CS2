import pyautogui
import time
from colorama import Fore, Style
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def check_for_image(image):
    x, y = pyautogui.locateCenterOnScreen(image)
    pyautogui.click(x, y)
    sys.exit()


def main():
    print(Fore.GREEN + "Auto Accept Script by: @Nasenhut" + Style.RESET_ALL)
    print(Fore.GREEN + "Auto Accepting Queue" + Style.RESET_ALL)
    print(Fore.GREEN + "Looking for Accept Button" + Style.RESET_ALL)
    print(Fore.GREEN + "Close this to stop" + Style.RESET_ALL)
    while True:
        try:
            check_for_image(resource_path(image_name))
        except pyautogui.ImageNotFoundException:
            print(Fore.RED + "Accpept Button not found" + Style.RESET_ALL)
            print(Fore.RED + "Trying again in 2 Seconds" + Style.RESET_ALL)
            time.sleep(2)


if __name__ == "__main__":
    image_name = "accept.png"
    my_path = os.path.dirname(os.path.realpath(__file__))

    os.chdir(my_path)
    main()
