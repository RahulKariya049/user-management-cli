from colorama import Fore,Style
from os import system,name

color_map = {
    "RED" : Fore.RED,
    "GREEN" : Fore.GREEN,
    "MAGENTA" : Fore.MAGENTA,
    "CYAN" : Fore.CYAN
}
def my_print(text : str, colour = "WHITE", bold = False) -> None:
    Colour_code = color_map.get(colour , Fore.WHITE)
    style = Style.BRIGHT if bold else ""
    print(style + Colour_code + text + Style.RESET_ALL)

def clear_screen() -> None:
    system('cls' if name == 'nt' else 'clear')
