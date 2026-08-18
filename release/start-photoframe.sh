#!/bin/bash

cd /home/david/photoframe

/usr/bin/python3 -m updater.updater_app \
    >> /home/david/photoframe/logs/startup.log 2>&1