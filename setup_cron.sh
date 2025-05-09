#!/bin/bash

# Get the absolute path of the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Create the crontab entry
(crontab -l 2>/dev/null; echo "*/5 * * * * cd $SCRIPT_DIR && source venv/bin/activate && python oscar_scraper.py >> scraper.log 2>&1") | crontab -

echo "Crontab has been set up to run the scraper every 5 minutes"
echo "You can check the logs in scraper.log" 