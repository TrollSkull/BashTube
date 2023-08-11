import requests, urllib.request, sys
from lib.core.utils import Colors
from lib.core.wifi import check_wifi
from lib.core.utils import Utils

URL = "https://raw.githubusercontent.com/TrollSkull/BashTube/master/"

def update():
    files = ['bashtube.py', 'lib/core/wifi.py', 'lib/core/updater.py', 'lib/core/version',
             'lib/core/utils.py', 'lib/main.py', 'lib/core/exceptions.py', 'requirements.txt',
             'lib/core/downloader.py', 'lib/.config']

    for fl in files:
        data = urllib.request.urlopen(URL + fl).read()

        with open(fl, "wb") as file:
            file.write(data)

    print(Colors.OK + "\n[BashTube]" + Colors.RESET + " Updated successfull, exiting script.")
    sys.exit(0)

def check_version():
    try:
        tool_version = open("./lib/core/version", "r",
                            encoding = 'utf-8').read()
    except FileNotFoundError:
        tool_version = "1.0"

    try:
        check_wifi()
        git_version = requests.get(
            "https://raw.githubusercontent.com/TrollSkull/BashTube/main/lib/core/version",
            timeout = 60).text

    except Exception as err:
        import sys

        print(err, file=sys.stderr)
        sys.exit(1)

    print(Colors.WORKING + "\n[BashTube]" + Colors.RESET +" Verifying Git version...")

    if tool_version == git_version:
        print(Colors.WARNING + "\n[BashTube]" + Colors.RESET +
              " Version match with GitHub repository.")

    else:
        print(Colors.WORKING + "\n[BashTube]" + Colors.RESET +
              " Update available, downloading " + Colors.WORKING + "(" +
              Colors.OK + Utils.GIT_VERSION + Colors.WORKING + ")...")

        update()
