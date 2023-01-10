#!/bin/bash

DIR="/home/ubuntu/Flask-App"
if [ -d "$DIR" ]; then
    echo "$DIR" exists:
else
    echo "Creating $DIR directory"
    mkdir $DIR

cd /home/ubuntu/Flask-App
sudo nohup python3 main.py > /dev/null 2>&1 &