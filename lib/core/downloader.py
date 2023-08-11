from lib.core.utils import Colors
from pytube import YouTube
import json

with open('lib/config.json', 'r', encoding = 'utf-8') as file:  
    config = json.load(file)

videoquality = config["Script Configuration"]["videoquality"]

def get_itag(resolution_from_file):
    if resolution_from_file in ["low", "360", "360p"]:
        itag = 18

    elif resolution_from_file in ["medium", "720", "720p", "hd"]:
        itag = 22

    elif resolution_from_file in ["high", "1080", "1080p",
                        "fullhd","full_hd", "full hd"]:
        itag = 137

    elif resolution_from_file in ["very high", "2160",
                        "2160p", "4K", "4k"]:
        itag = 313

    else:
        itag = 22

    return itag

def download_from_youtube(req_url, req_res):
    itag = get_itag(req_res)
    ytdwld = YouTube(req_url)

    ytstream = ytdwld.streams.get_by_itag(itag)
    ytstream.download()

    return ytstream.default_filename

def download_video(urls):
    for url in urls:
        try:
            print(Colors.WORKING + "\n[BashTube] " + Colors.RESET + "Downloading video...")
            download_from_youtube(url, videoquality)

        except Exception:
            print(Colors.WARNING + "\n[BashTube] " + Colors.RESET +
                  "User resolution falied, change your configurations now!")
