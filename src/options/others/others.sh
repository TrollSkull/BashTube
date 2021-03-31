#!/bin/bash

R='\033[31m'
GRE='\033[32m'
W='\033[37m'
B='\033[34m'
GRA='\033[1;30m'
Y='\033[1;33m'
C='\033[1;36m'

echo "[i] Try downloading and testing my repositories"
echo
echo -e ${R}"[01] ${W}MorseTranslator"
echo -e ${R}"[02] ${W}FileEditor"
echo -e ${R}"[00] ${W}Back"
echo
read -p "BashTube/Others >> " tools

    if [ "$tools" = "1" ]||[ "$tools" = "01" ]; then
        echo
        echo -e ${W}"What is ${R}MorseTranslator${W}?"
        echo
        echo "MorseTranslator is a morse code translator"
        echo "made in Python"
        echo
        read -p "[?] Do you want to install this tool? (y/n): " yes01

            if [ "$yes01" == "y" ]; then
                cd programs

                bash 01.sh

                exit

            else
                echo
                echo -e ${Y}"[!] ${W}Tool not installed"

                sleep 2
                exit
            fi

    elif [ "$tools" = "2" ]||[ "$tools" = "02" ]; then
        echo
        echo -e ${W}"What is ${R}FileEditor${W}?"
        echo
        echo "FileEditor is a text editor which can"
        echo "create and modify files, made in Python"
        echo
        read -p "[?] Do you want to install this tool? (y/n): " yes02

            if [ "$yes02" == "y" ]; then
                cd programs

                bash 02.sh

                exit

            else
                echo
                echo -e ${Y}"[!] ${W}Tool not installed"

                sleep 2
                exit
            fi

    else
            exit
    fi