#!/bin/bash

echo "Stop any exist main.py"


sudo pgrep -f  "main.py" | xargs kill -9
sudo chmod -R 777 /home/ubuntu/Flask-App