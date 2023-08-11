from lib.core.exceptions import BashTubeExceptions
from lib.core.wifi import check_wifi
from lib.core.utils import print_banner, move_videos, check_os_clear, Colors
from lib.core.downloader import download_video
from lib.core.updater import check_version
import time
import json
import sys

def BashTube():
    try:
        check_os_clear()
        print_banner()
        check_wifi()

    except Exception as err:
        from lib.core.exceptions import BashTubeExceptions
        raise BashTubeExceptions(str(err))

    while True:
        try:
            option = str(input(Colors.WORKING + "\nBashTube " + Colors.FAIL + "~# " + Colors.RESET))

            if option == "1":

                url = input(Colors.FAIL + "\n[BashTube] " + Colors.RESET +
                            "Enter a URL to start downloading: ")

                try:
                    check_wifi()
                    print(Colors.WORKING)

                    download_video(url)
                    move_videos()

                except Exception as err:
                    print(Colors.FAIL + "\n[BashTube] " + Colors.RESET +
                          "An error has closed the script.")

                    print(err)
                    sys.exit(1)

            elif option == "2":
                check_version()

            elif option == "3":
                quality_req = input(Colors.OK + "\n[BashTube] " + Colors.RESET +
                             "Set a video quality (720p, 480p, medium, hd, etc.): ")

                with open('lib/config.json', 'r', encoding = 'utf-8') as file:
                    config = json.load(file)

                config["Script Configuration"]["videoquality"] = quality_req

                print(Colors.OK + "[BashTube] " + Colors.RESET +
                      "User quality configuration changed to: "+ quality_req + ", saving...")

                with open('lib/config.json', 'w', encoding = 'utf-8') as file:
                    json.dump(config, file, indent = 4)

            elif option == "4":
                print(Colors.WORKING + "\n[BashTube] " + Colors.RESET + "Bye bye!")
                sys.exit(0)

            else:
                print(Colors.FAIL + "\n[BashTube] " + Colors.RESET + "Command not found!")
                time.sleep(2)

        except KeyboardInterrupt:
            print (Colors.WARNING + "\n[BashTube] " + Colors.RESET + "Keyboard interrupt detected, exiting.")
            sys.exit(1)

def main():
    try:
        BashTube()

    except Exception as err:
        import sys

        print(err, file=sys.stderr)
        sys.exit(1)
