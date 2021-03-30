import time, sys, os
import urllib.request

option = 1
more = ""

def dwl_img(url):
    file = "img.jpg"
    try:
        r = urllib.request.urlopen(url)
        f = open(file, "wb")
        f.write(r.read())
        f.close
    except Exception:
        print("") # Space
        print ("Err. 1: No link has been put")
        time.sleep(2)
    
while(option == int(1)):
    print("") # Space
    url = str(input("Copy & Paste the URL of the image: "))
    
    dwl_img(url)

    print("") # Space
    more = str(input("Do you want to download more images? (y/n): "))
    if more == "y":
        option = 1

    elif more == "n":
        option = 0

    else:
        option = 1

        print("") # Space
        print ("There is no such option, please enter a valid option.")