import sys
from modules.osDetection import osDetection
from modules.portScanner import portScan
from modules.STBuster import STBuster_

class style():
    RED = lambda x: '\033[31m' + str(x)
    GREEN = lambda x: '\033[32m' + str(x)
    YELLOW = lambda x: '\033[33m' + str(x)
    BLUE = lambda x: '\033[34m' + str(x)
    CYAN = lambda x: '\033[36m' + str(x)
    RESET = lambda x: '\033[0m' + str(x)


def main():
    while True:
        print (u"{}[2J{}[;H".format(chr(27), chr(27)))
        print(style.YELLOW('[!]') + style.RESET(' Welcome to Scan the Box.'))
        print(style.GREEN('\n[+]') + style.RESET('Choose the number of the tool you want to use:\n    1) Port Scanner.\n    2) OS Detection Scanner.\n    3) Directories/Files BruteForce.\n    4) Exit.'))
        mode = str(input(style.CYAN('\n>>> ') + style.RESET('')))

        portScan() if mode == "1" else osDetection() if mode == "2" else STBuster_() if mode == "3" else sys.exit()

if __name__ == "__main__":
    main()
