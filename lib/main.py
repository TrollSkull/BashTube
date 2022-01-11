try:
    import os
    import sys
    import time
    import argparse
    import youtube_dl
    from lib.core.wifi import CheckWifi

except Exception as err:
    from lib.core.exceptions import BashTubeExceptions
    raise BashTubeExceptions(str(err))

class Main:
    try:
        from lib.core.exceptions import BashTubeExceptions
        from lib.core.wifi import CheckWifi
        from lib.core.banner import PrintBanner
        from lib.core.banner import Colors
    except Exception as err:
        import sys

        print(err, file=sys.stderr)
        sys.exit(1)

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

                    print(Colors.RESET)    
                    if sys.platform == "win32":
                        os.system("MOVE *.mp4 downloaded")
                        print(Colors.OK + "\n[BashTube] " + Colors.RESET + "Video moved to '/BashTube/downloaded'.")
                        sys.exit(1)
                    else:
                        os.system("mv *.mp4 downloaded")
                        print(Colors.OK + "\n[BashTube] " + Colors.RESET + "Video moved to '/BashTube/downloaded'.")
                        sys.exit(1)
                    
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
