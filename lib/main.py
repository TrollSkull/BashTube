class Main:
    try:
        from lib.core.exceptions import BashTubeExceptions
        from lib.core.wifi import CheckWifi
        from lib.core.utils import PrintBanner, MoveVideos, CheckOSClear, Colors
        from lib.core.downloader import DownloadVideo
        from lib.core.updater import CheckVersion
        import time, sys, configparser

        CheckOSClear()
        PrintBanner()
        CheckWifi()

    except Exception as err:
        from lib.core.exceptions import BashTubeExceptions
        raise BashTubeExceptions(str(err))

    while True:
        try:
            option = str(input(Colors.WORKING + "\nBashTube " + Colors.FAIL + "~# " + Colors.RESET))
                
            if option == "1":

                URL = input(Colors.FAIL + "\n[BashTube] " + Colors.RESET + "Enter a URL to start downloading: ")

                try:
                    CheckWifi()
                    print(Colors.WORKING)  

                    DownloadVideo(URL)
                    MoveVideos()
                        
                except Exception as err:
                    print(Colors.FAIL + "\n[BashTube] " + Colors.RESET + "An error has closed the script.")
                    print(err)
                    sys.exit(1)

            elif option == "2":
                CheckVersion()

            elif option == "3":
                CONF = input(Colors.OK + "\n[BashTube] " + Colors.RESET + "Set a video quality (720p, 480p, etc.): ")
                
                config = configparser.ConfigParser()
                config['Script Configuration'] = {'videoQuality': CONF}

                print(Colors.OK + "[BashTube] " + Colors.RESET + "User quality configuration changed to: " + CONF + ", saving...")
                
                with open('lib/.config', 'w') as configfile:
                    config.write(configfile)

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
        bashtube = Main()
        bashtube
    except Exception as err:
        import sys

        print(err, file=sys.stderr)
        sys.exit(1)