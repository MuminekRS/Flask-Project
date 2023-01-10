#!/bin/bash

echo "Stop any exist main.py"


ps -auf | grep main.py | sudo awk  '{system("sudo kill -9 "$2)}' > /dev/null 2>&1 &
sudo chmod -R 777 /home/ubuntu/Flask-App