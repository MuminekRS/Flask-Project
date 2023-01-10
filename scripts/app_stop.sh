#!/bin/bash

echo "Stop any exist main.py"
sudo pgrep -f  "main.py" | xargs kill -9