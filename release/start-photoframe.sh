#!/bin/bash

cd /home/pi/photoframe
mkdir -p logs
/usr/bin/python3 -m updater.updater_app \
    >> /home/pi/photoframe/logs/startup.log 2>&1