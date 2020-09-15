#!/bin/bash

umacro_version="v0.0.2"

[[ -d /etc/umacro/ ]] || mkdir /etc/umacro
[[ -f /etc/umacro/umacro_conf.yml ]] || touch /etc/umacro/umacro_conf.yml

[[ -f /usr/local/bin/umacro ]] && rm /usr/local/bin/umacro

wget -P /usr/local/bin https://github.com/dhsathiya/UMacro/releases/download/$umacro_version/umacro -q --show-progress

chmod +x /usr/local/bin/umacro

read -n 1 -p "Do you want to install xdotool for better support? [y/n]:" install_xdotool 

if [[ $install_xdotool == "y" ]]; then
	apt update
	apt install xdotool --yes
fi


echo -e "\nInstallation of UMacro has been completed."
