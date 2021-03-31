#!/bin/bash

GRE='\033[32m'
W='\033[37m'

cd
echo
git clone https://github.com/TrollSkull/FileEditor.git &> /dev/null
echo -e ${GRE}"[+] ${W}Tool Installed!"
echo
read -p "[?] Do you want to run the installed tool? (y/n): " entry

if [ "$entry" == "y" ]; then
    echo
    cd
    cd FileEditor
    python editor.py

else
    echo
    echo -e ${GRE}"[+] ${W}FileEditor installed!"
    echo
    sleep 1
fi