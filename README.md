# OSCAR Course Availability Checker

this script monitors a specific course in Georgia Tech's OSCAR system and notifies you when a spot becomes available

## setup

1. install the required dependencies:
```bash
pip install -r requirements.txt
```

2. run the script:
```bash
python oscar_scraper.py
```

## features

- checks course availability every 5 minutes
- sends desktop notifications when a spot opens up
- logs all activity to `scraper.log`
- displays current enrollment status in the console

## notes

- the script will continue running until a spot becomes available
- uou can modify the check interval by changing the `time.sleep()` value in the script
- the script uses desktop notifications, so make sure your system supports them
- all errors and activities are logged to `scraper.log` for debugging purposes
