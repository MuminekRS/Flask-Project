#!/bin/bash

DIR="/home/ubuntu/Flask-Project"
if [ -d "$DIR" ]: then
    echo "$DIR" exists:
else
    echo "Creating $DIR directory"
    mkdir $DIR

sudo chmod -R 777 /home/ubuntu/Flask-Project
cd /home/ubuntu/Flask-Project
nohup python3 main.py > /dev/null 2>&1 &