#!/bin/bash

echo "Stop any exist main.py and chande mode for DIR"


sudo pgrep -f  "main.py" | xargs kill -9 > /dev/null 2>&1 &:
sudo chmod -R 777 /home/ubuntu/Flask-App