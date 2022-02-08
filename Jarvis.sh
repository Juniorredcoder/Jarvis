#!/bin/bash
# Update Script for Termux_welcome v2.1-Stable
# Script created by @certified_youtuber


dependencies() {

command -v git > /dev/null 2>&1 || { echo >&2 "Package GIT is not installed ... Unable to update ..."; exit 1; }

}

script() {

clear
printf "\n \e[1;92mLoading \e[1;94m\e[1;92m ...\n\n"
sleep 1.5
printf "\n\e[1;92mstarting ...\n\e[0m"
printf "Jarvis:"
figlet Welcome | lolcat
play-audio Jarvis.mp3
clear
figlet Jarvis | lolcat
python Jarvis.py
figlet Thank you | lolcat
}

dependencies
script
