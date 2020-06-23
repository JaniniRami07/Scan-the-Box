import sys
from modules.style import Style
from modules.osdetection import os_detection
from modules.portscanner import port_scan
from modules.stbuster import stbuster

def main():
    while True:
        try:
            print (u"{}[2J{}[;H".format(chr(27), chr(27)))
            print(Style.YELLOW('[!]') + Style.RESET(' Welcome to Scan the Box.'))
            print(Style.GREEN('\n[+]') + Style.RESET('Choose the number of the tool you want to use:\n    1) Port Scanner.\n    2) OS Detection Scanner.\n    3) Directories/Files BruteForce.\n    4) Exit.'))
            mode = str(input(Style.CYAN('\n>>> ') + Style.RESET('')))

            port_scan() if mode == "1" else os_detection() if mode == "2" else stbuster() if mode == "3" else sys.exit()
        except KeyboardInterrupt:
                print(Style.RED('\n[!]') + Style.RESET(' User exit.'))
                sys.exit()

if __name__ == "__main__":
    main()
