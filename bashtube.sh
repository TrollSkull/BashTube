#!/bin/bash

# Tool Name: BashTube
# Author: TrollSkull
# Date: 29/03/2021

R='\033[31m'
GRE='\033[32m'
W='\033[37m'
B='\033[34m'
GRA='\033[1;30m'
Y='\033[1;33m'
C='\033[1;36m'

clear

function banner () {
        echo -e ${R}""
        cd src
        cat banner.txt
        cd ..
        echo
        echo -e ${R}" BashTube: ${W}https://github.com/TrollSkull/BashTube"
        echo
}

function call_banner () {
        clear
        banner
}

function mv_videos () {
        mv *.mp4 /data/data/com.termux/files/home/storage/downloads
}

function mv_images () {
        mv *.jpg /data/data/com.termux/files/home/storage/downloads
}

call_banner

start="1" # Exit switch
while [ "$start" = "1" ]
do
    
    read -p "BashTube >> " entry

    if [ "$entry" == "help" ]; then
            call_banner

	    cd src
            cd options
	    bash help.sh

	    cd ..
            cd ..

    elif [ "$entry" == "video" ]; then
            call_banner

            cd src
            cd core
            python video.py

            mv_videos

	    cd ..
            cd ..

            call_banner

    elif [ "$entry" == "image" ]; then
            call_banner

            cd src
            cd core
            python image.py

            mv_images

	    cd ..
            cd ..

            call_banner

    elif [ "$entry" == "change log" ]; then
            call_banner

            cd src
            cd options
            bash change.sh

            cd ..
            cd ..

    elif [ "$entry" == "others" ]; then
            call_banner

            cd src
            cd options
            cd others
            bash others.sh

            cd ..
            cd ..
            cd ..

            call_banner

    elif [ "$entry" == "update" ]; then

            call_banner

	    echo -e ${Y}"[!] ${W}It will be updated to the most recent version of the tool, if"
	    echo "you already have the latest version, it will be downloaded again"
            echo

            read -p "[?] Do you wanna update the tool? (y/n): " update
            echo

            if [ "$update" == "y" ]||[ "$update" == "Y" ]; then
                echo -e ${B}"[*] ${W}Updating..."
                
                cd ..
                rm -rf BashTube

                git clone http://github.com/TrollSkull/BashTube &> /dev/null
                cd BashTube
                bash installer.sh

                exit

            elif [ "$update" == "n" ]||[ "$update" == "N" ]; then
                echo -e ${Y}"[-] ${W}Update canceled"
                sleep 2

                call_banner

            else
                echo -e ${R}"[!] ${W}That option does not exist"
                sleep 2

                call_banner

            fi
        
    elif [ "$entry" == "about" ]; then
            call_banner

            cd src
            cd options
            bash about.sh
            cd ..
            cd ..

    elif [ "$entry" == "exit" ]; then
            echo
            echo -e ${W}"Thanks for using ${R}BashTube${W}, I hope you enjoyed this tool :)"

            sleep 3
            clear
            exit

    else
            echo
            echo -e ${R}"[!] ${W}Command not found, type ${R}help ${W}for commands"
            sleep 2

            call_banner
    fi 

done
