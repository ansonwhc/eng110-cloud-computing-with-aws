#!/bin/bash

sudo apt update -y
sudo apt upgrade -y

sudo apt install python -y
sudo apt install python3-pip -y
alias python=python3
export python=python3
sudo python3 -m pip install awscli
pip3 install boto3