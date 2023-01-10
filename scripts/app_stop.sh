#!/bin/bash

echo "Stop any exist main.py"
sudo rm -r /home/ubuntu/*
sudo pgrep -f  "main.py" | xargs kill -9