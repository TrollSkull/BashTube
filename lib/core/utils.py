import os, sys

class Colors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    WORKING = '\033[34m'

def MoveVideos():
    print(Colors.RESET)

    if sys.platform == "win32":
        os.system("MOVE *.mp4 downloaded")
        print(Colors.OK + "\n[BashTube] " + Colors.RESET + "Video moved to '/BashTube/downloaded'.")
        sys.exit(1)

    else:
        os.system("mv *.mp4 downloaded")
        print(Colors.OK + "\n[BashTube] " + Colors.RESET + "Video moved to '/BashTube/downloaded'.")
        sys.exit(1)

def PrintBanner():
    if sys.platform == "win32":
        os.system("cls")
        print(Colors.WORKING + "   ___           __" + Colors.FAIL + "  ______     __            ")
        print(Colors.WORKING + "  / _ )___ ____ / /" + Colors.FAIL + " /_  __/_ __/ /  ___       ")
        print(Colors.WORKING + " / _  / _ `(_-</ _\ " + Colors.FAIL + " / / / // / _ \/ -_)      ")
        print(Colors.WORKING + "/____/\_,_/___/_//_/" + Colors.FAIL + " /_/  \_,_/_.__/\__/   " + Colors.RESET + "v2.1")
        print(Colors.RESET)     
        print(chr(27)+"[1;37m"+"[i] Press CTRL+C to stop the script." + Colors.RESET)

    else:
        os.system("clear")
        print(Colors.WORKING + "   ___           __" + Colors.FAIL + "  ______     __            ")
        print(Colors.WORKING + "  / _ )___ ____ / /" + Colors.FAIL + " /_  __/_ __/ /  ___       ")
        print(Colors.WORKING + " / _  / _ `(_-</ _\ " + Colors.FAIL + " / / / // / _ \/ -_)      ")
        print(Colors.WORKING + "/____/\_,_/___/_//_/" + Colors.FAIL + " /_/  \_,_/_.__/\__/   " + Colors.RESET + "v2.1")
        print(Colors.RESET) 
        print(chr(27)+"[1;37m"+"[i] Press CTRL+C to stop the script." + Colors.RESET)     