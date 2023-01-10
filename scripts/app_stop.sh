#!/bin/bash

echo "Stop any exist main.py"


pgrep -f  "main.py" | xargs kill -9 > /dev/null 2>&1 &
chmod -R 777 /home/ubuntu/Flask-App