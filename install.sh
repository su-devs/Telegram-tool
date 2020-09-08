#!/bin/bash
#code by g1ng3rbite (kevo)
clear
toilet --gay -f smblock Telegram-tool
echo -e "Script by g1ng3rb1t3"
if [[ -s requirements.set ]];then
echo "All Requirements Found"
echo "openning config file"
sleep 2
python3 config.py
else
echo 'Installing Requirements....'
echo 
echo 
pkg install python
pkg install toilet
pkg install figlet
apt install python3-pip
pip install telethon
pip install colorama
pip install progressbar
echo This script is made by kelvin >requirements.set
fi
