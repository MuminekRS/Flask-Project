#!/bin/bash
DIR="/home/ubuntu/Flask-App"

echo "Stop any exist main.py"
DIR="/home/ubuntu/Flask-App"
if [ -d "$DIR" ]; then
    echo "$DIR" exist:
else
    echo "Creating $DIR directory"
    mkdir $DIR
fi



ps -auf | grep main.py | sudo awk  '{system("sudo kill -9 "$2)}' > /dev/null 2>&1 &
sudo chmod -R 777 /home/ubuntu/Flask-App