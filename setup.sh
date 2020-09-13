#!/bin/bash

umacro_version="v0.0.2"

mkdir /etc/umacro
touch /etc/umacro/umacro_conf.yml

wget -P /usr/local/bin https://github.com/dhsathiya/UMacro/releases/download/$umacro_version/umacro -q --show-progress
chmod +x /usr/local/bin/umacro

