#!/bin/bash

DIR="/home/ubuntu/Flask-App"
if [ -d "$DIR" ]; then
    echo "$DIR" exists:
else
    echo "Creating $DIR directory"
    mkdir $DIR
fi

cd /home/ubuntu/Flask-App
sudonohup python3 main.py > /dev/null 2>&1 &