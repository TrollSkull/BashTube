class Main:
    try:
        from lib.core.exceptions import BashTubeExceptions
        from lib.core.wifi import CheckWifi
        from lib.core.utils import PrintBanner, MoveVideos, Colors

        import os
        import sys
        import time
        import youtube_dl
    except Exception as err:
        from lib.core.exceptions import BashTubeExceptions
        raise BashTubeExceptions(str(err))


    while True:
        try:
            PrintBanner()
            URL = input("Enter a URL to start downloading: ")

            try:
                CheckWifi()
                print(Colors.WORKING)    
                YoutubeOptions = {}
                zxt = URL.strip()

                with youtube_dl.YoutubeDL(YoutubeOptions) as ydl:
                    ydl.download([zxt])
                    MoveVideos()
                    
            except Exception as err:
                print(Colors.FAIL + "\n[BashTube] " + Colors.RESET + "An error has closed the program.")
                sys.exit(1)

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
