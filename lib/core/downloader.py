from lib.core.utils import Colors
from pytube import YouTube
import configparser

# Open "lib/.config" file and get the configurations.
config = configparser.ConfigParser()
config.read('lib/.config')

# Getting quality from ".config" file.
videoQuality = config.get('Script Configuration', 'videoQuality')

# Download videos with pytube.
def DownloadVideo(URL):
    yt = YouTube(URL)
    
    try:
        # Downloading video with user resolution.
        print(Colors.WORKING + "\n[BashTube] " + Colors.RESET + "Downloading video...")
        yt.streams.get_by_resolution(resolution=str(videoQuality)).download()

    except Exception:
        # Downloading video with default resolution.
        print(Colors.WARNING + "\n[BashTube] " + Colors.RESET + "User resolution falied, change your configurations now!")
        print(Colors.WORKING + "\n[BashTube] " + Colors.RESET + "Downloading video with default configuration...")
        yt.streams.get_highest_resolution().download()