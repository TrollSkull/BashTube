import os, sys

class Colors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    WORKING = '\033[34m'

def PrintBanner():
    if sys.platform == "win32":
        os.system("cls")
        print(Colors.WORKING + "   ___           __" + Colors.FAIL + "  ______     __            ")
        print(Colors.WORKING + "  / _ )___ ____ / /" + Colors.FAIL + " /_  __/_ __/ /  ___       ")
        print(Colors.WORKING + " / _  / _ `(_-</ _\ " + Colors.FAIL + " / / / // / _ \/ -_)      ")
        print(Colors.WORKING + "/____/\_,_/___/_//_" + Colors.FAIL + " /_/  \_,_/_.__/\__/   " + Colors.RESET + "v2.0 B")
        print(Colors.RESET)     
        print("[i] Press CTRL+C to stop the script.")

    else:
        os.system("clear")
        print(Colors.WORKING + "   ___           __" + Colors.FAIL + "  ______     __            ")
        print(Colors.WORKING + "  / _ )___ ____ / /" + Colors.FAIL + " /_  __/_ __/ /  ___       ")
        print(Colors.WORKING + " / _  / _ `(_-</ _\ " + Colors.FAIL + " / / / // / _ \/ -_)      ")
        print(Colors.WORKING + "/____/\_,_/___/_//_" + Colors.FAIL + " /_/  \_,_/_.__/\__/   " + Colors.RESET + "v2.0 B")
        print(Colors.RESET) 
        print("[i] Press CTRL+C to stop the script.")   
