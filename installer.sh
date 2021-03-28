#!/bin/bash

# Tool Name: BashTube (Installer)
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
rm -rf README.md
rm -rf LICENSE
rm -rf installer.sh
rm -rf resources

echo -e ${B}"[*] ${W}Storage access required for downloaded videos."

termux-setup-storage
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

banner

echo -e ${B}"[*] ${W}Updating Git..."
pkg install -y git &> /dev/null

echo -e ${GRE}"[+] ${W}Done!"

echo -e ${B}"[*] ${W}Updating Python..."
pkg install -y python &> /dev/null
pkg install -y python2 &> /dev/null
python -m pip install --upgrade pip &> /dev/null

echo -e ${GRE}"[+] ${W}Done!"

echo -e ${B}"[*] ${W}Downloading resources..."
pip install youtube_dl &> /dev/null

echo -e ${GRE}"[+] ${W}Done!"

sleep 2

bash bashtube.sh

exit
