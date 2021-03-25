import time, sys, os
import youtube_dl

ydl_opts = {}

def dwl_vid():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])

option = 1
channel = 1
more = ""

while(option == int(1)):
    while(channel == int(1)):
        print("") # Space
        link_of_video = input("Copy & Paste the URL of the video: ")
        zxt = link_of_video.strip()

        print("") # Space
        
        dwl_vid()

        print("") # Space

        more = str(input("Do you want to download more videos? (y/n): "))
        if more == "y":
            option = 0
            channel = 1
            
        elif more == "n":
            option = 0
            channel = 0

        else:
            option = 1

            print("") # Space

            print ("There is no such option, please enter a valid option.")