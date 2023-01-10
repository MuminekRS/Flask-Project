#!/bin/bash

DIR="/home/ubuntu/Flask-App"
if [ -d "$DIR" ]: then
    echo "$DIR" exists:
else
    echo "Creating $DIR directory"
    mkdir $DIR

sudo chmod -R 777 /home/ubuntu/Flask-App
cd /home/ubuntu/Flask-App
sudo nohup python3 main.py > /dev/null 2>&1 &