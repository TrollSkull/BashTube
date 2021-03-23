#!/bin/bash

# Tool Name: BashTube
# Author: TrollSkull
# Date: 23/03/2021

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
        cat ban
        cd ..
        echo
        echo -e ${R}" BashTube: ${W}https://github.com/TrollSkull/BashTube"
        echo
}

clear
banner

start="1" # Exit switch
while [ "$start" = "1" ]
do
    
    read -p "BashTube >> " entry

    if [ "$entry" == "help" ]; then
            clear
	    banner

	    cd src
            cd options
	    bash com.sh
	    cd ..
            cd ..

    elif [ "$entry" == "convert" ]; then
            clear
	    banner

            cd src
            python core.py
	    cd ..

            clear
            banner

    elif [ "$entry" == "update" ]; then

            clear
            banner

	    echo -e ${Y}"[!] ${W}It will be updated to the most recent version of the tool, if"
	    echo "you already have the latest version, it will be downloaded again."
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
                echo -e ${Y}"[-] ${W}Update canceled."
                sleep 2
                clear
                banner

            else
                echo -e ${R}"[!] ${W}That option does not exist."
                sleep 2
                clear
                banner

            fi
        
    elif [ "$entry" == "about" ]; then
            clear
            banner

            cd src
            cd options
            bash about.sh
            cd ..
            cd ..

    elif [ "$entry" == "exit" ]; then
            echo
            echo -e ${W}"Thanks for using ${R}BashTube${W}, we hope you enjoyed it :)"

            sleep 3
            clear
            exit

    else
            echo
            echo -e ${R}"[!] ${W}Command not found, type ${R}help ${W}for commands."
            sleep 2
            clear
            banner
    fi 

done