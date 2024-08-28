#!/bin/sh
# This is a comment!

apt update -y
apt upgrade -y
apt install software-properties-common -y
apt install python3 -y
apt-get install python3-pyaudio portaudio19-dev net-tools -y
python3 -m ensurepip --default-pip
pip install -r requirements.txt