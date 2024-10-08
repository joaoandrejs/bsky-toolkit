from colorama import Fore
import os


def clear():
    if os.name == 'nt':  # Windows
        os.system("cls")
    else:  # Unix/MacOS
        os.system("clear")


def logo():
    print(f"""{Fore.BLUE}
  ____    _        _    _   ______    _____   _  __ __     __
 |  _ \\  | |      | |  | | |  ____|  / ____| | |/ / \\ \\   / /
 | |_) | | |      | |  | | | |__    | (___   | ' /   \\ \\_/ /
 |  _ <  | |      | |  | | |  __|    \\___ \\  |  <     \\   /
 | |_) | | |____  | |__| | | |____   ____) | | . \\     | |
 |____/  |______|  \\____/  |______| |_____/  |_|\\_\\    |_|  {Fore.RESET}""")


def centralized(text):
    print(f"{text: ^60}{Fore.RESET}")
