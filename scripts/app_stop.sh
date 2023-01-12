#!/bin/bash
DIR="/home/ubuntu/Flask-App"

echo "Stop any exist main.py"
DIR="/home/ubuntu/Flask-App"
if [ -d "$DIR" ]; then
    echo "$DIR exist"
else
    echo "Creating $DIR directory"
    mkdir $DIR
fi