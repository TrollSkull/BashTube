import os, sys, requests

class Colors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    WORKING = '\033[34m'

class Utils:
    TOOL_VERSION = open("./lib/core/version", "r").read()
    GIT_VERSION = requests.get("https://raw.githubusercontent.com/TrollSkull/SMSBOX/main/lib/core/version").text  

def CheckOSClear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

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
    print(Colors.WORKING + "   ___           __ " + Colors.FAIL + " ______     __            ")
    print(Colors.WORKING + "  / _ )___ ____ / / " + Colors.FAIL + "/_  __/_ __/ /  ___       ")
    print(Colors.WORKING + " / _  / _ `(_-</ _ \ " + Colors.FAIL + "/ / / // / _ \/ -_)      ")
    print(Colors.WORKING + "/____/\_,_/___/_//_/" + Colors.FAIL + "/_/  \_,_/_.__/\__/   " + Colors.RESET + "v3.0\n")

    print(Colors.WORKING + "[" + Colors.RESET + "1" + Colors.WORKING + "] Download" + Colors.RESET + "           -   " + Colors.FAIL + "Download a video!")
    print(Colors.WORKING + "[" + Colors.RESET + "2" + Colors.WORKING + "] Update script" + Colors.RESET + "      -   " + Colors.FAIL + "Version (" + Colors.WORKING + Utils.TOOL_VERSION + Colors.FAIL + ")")
    print(Colors.WORKING + "[" + Colors.RESET + "3" + Colors.WORKING + "] Edit Configuration" + Colors.RESET + " -   " + Colors.FAIL + "Edit user configuration!" + Colors.RESET)
    print(Colors.WORKING + "[" + Colors.RESET + "4" + Colors.WORKING + "] Exit" + Colors.RESET + "               -   " + Colors.FAIL + "Close script!" + Colors.RESET)