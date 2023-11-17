import sys
from pyfiglet import Figlet
import random as rdm

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    len_argv = len(sys.argv)
    if len_argv == 3:
        argument = sys.argv[1]
        font = sys.argv[2]
        if argument in ["-f", "--font"] and font in fonts:
            str_input = input("Input: ")
            return_response(str_input, font, figlet)
        else:
            invalid_usage()
    elif len_argv == 1:
        str_input = input("Input: ")
        font = rdm.choice(fonts)
        return_response(str_input, font, figlet)
    else:
        invalid_usage()

def invalid_usage():
    sys.exit("Invalid usage")

def return_response(str_input, font, figlet):
    figlet.setFont(font = font)
    print(figlet.renderText(str_input))

if "__main__" == __name__:
    main()