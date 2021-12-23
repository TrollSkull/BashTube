import os, sys

class Colors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'

def PrintBanner():
    if sys.platform == "win32":
        os.system("cls")
        print(Colors.FAIL + "   ___           __ ______     __            ")
        print("  / _ )___ ____ / //_  __/_ __/ /  ___         ")
        print(" / _  / _ `(_-</ _ \/ / / // / _ \/ -_)        ")
        print("/____/\_,_/___/_//_/_/  \_,_/_.__/\__/   v1.4 A")
        print(Colors.RESET)     

    else:
        os.system("clear")
        print(Colors.FAIL + "   ___           __ ______     __            ")
        print("  / _ )___ ____ / //_  __/_ __/ /  ___         ")
        print(" / _  / _ `(_-</ _ \/ / / // / _ \/ -_)        ")
        print("/____/\_,_/___/_//_/_/  \_,_/_.__/\__/   v1.4 A")
        print(Colors.RESET)     
