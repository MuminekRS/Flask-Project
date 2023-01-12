#!/bin/bash
DIR="/home/ubuntu/Flask-App"


DIR="/home/ubuntu/Flask-App"
if [ -d "$DIR" ]; then
    echo "$DIR exist"
else
    echo "Creating $DIR directory"
    mkdir $DIR
fi

echo "Stop any exist main.py"

sudo rm -r /home/ubuntu/*
sudo ps -auf | grep main.py | sudo awk  '{system("sudo kill -9 "$2)}' > /dev/null 2>&1 &
