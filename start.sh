#!/bin/sh

pip3 install --no-cache-dir -r requirements.txt && nodemon --exec python3 app.py > log.txt