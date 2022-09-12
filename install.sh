#!/bin/bash

echo "Starting Installation Process"

sudo apt update && sudo apt upgrade -y
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10 -y
apt install curl -y
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
apt install net-tools -y
apt install figlet -y
apt install tcpdump -y
pip3.10 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U 
pip3.10 install discord
pip3.10 install discord_webhooks
pip3.10 install requests
pip3.10 install psutil
pip3.10 install distro
pip3.10 install random
pip3.10 install platform
pip3.10 install date
pip3.10 install telepot
mkdir /root/pcaps

echo "Finished"
echo "Run 'python3.10 xloadv2.py' When You're Ready"