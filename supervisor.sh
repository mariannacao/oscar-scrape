#!/bin/bash

cd ~/oscar-scraper
source venv/bin/activate

while true; do
    echo "[$(date)] Starting oscar scraper..."
    python oscar_scraper.py
    
    echo "[$(date)] Scraper stopped. Restarting in 5 seconds..."
    sleep 5
done