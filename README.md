# oscar course availability checker

this script monitors a specific course in georgia tech's oscar system and notifies you via discord when a spot becomes available.

## setup

1. install the required dependencies:
```bash
pip install -r requirements.txt
```

2. set up discord notifications:
   - create a new discord server or use an existing one
   - create a new channel for notifications
   - right-click the channel → edit channel → integrations → create webhook
   - copy the webhook url

3. create a `.env` file:
   - copy `.env.example` to `.env`
   - paste your discord webhook url as the value for `discord_webhook_url`

4. test the notifications:
```bash
python test_notification.py
```

5. run the script:
```bash
python oscar_scraper.py
```

## features

- checks course availability every 5 minutes
- sends discord notifications when a spot opens up
- notifications include:
  - current enrollment status
  - number of remaining spots
  - direct link to register
  - timestamp
- logs all activity to `scraper.log`

## notes

- the script will continue running until a spot becomes available
- you can modify the check interval by changing the `time.sleep()` value in the script
- all errors and activities are logged to `scraper.log` for debugging purposes
- notifications can be received on both your phone and laptop through discord
