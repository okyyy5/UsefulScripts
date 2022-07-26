from termcolor import colored
import colorama

colorama.init()

def coloured_message(colour: str, text: str) -> str:
    return colored(text, colour)