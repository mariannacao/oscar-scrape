# oscar course availability checker

this script monitors a specific course in georgia tech's oscar system and notifies you via discord when a spot becomes available. it runs on a server with automatic restart capability.

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

## running locally

to run the script on your local machine:
```bash
python oscar_scraper.py
```

## running on server

the script is configured to run on a server with automatic restart capability. to deploy:

1. make sure you have ssh access to the server
2. run the deployment script:
```bash
./deploy.sh
```

the deployment script will:
- copy all necessary files to the server
- set up a python virtual environment
- install required dependencies
- start the scraper with automatic restart capability

## monitoring

to check the status of the scraper on the server:

```bash
# check supervisor logs (restart information)
ssh -p your-ssh-port your-username@your-server-ip "tail -f ~/oscar-scraper/supervisor.log"

# check scraper logs (course availability checks)
ssh -p your-ssh-port your-username@your-server-ip "tail -f ~/oscar-scraper/scraper.log"

# check if supervisor is running
ssh -p your-ssh-port your-username@your-server-ip "ps aux | grep supervisor.sh"
```

to stop the scraper:
```bash
ssh -p your-ssh-port your-username@your-server-ip "pkill -f supervisor.sh"
```

## features

- checks course availability every 5 minutes
- sends discord notifications when a spot opens up
- notifications include:
  - current enrollment status
  - number of remaining spots
  - direct link to register
  - timestamp
- runs on a server with automatic restart capability
- logs all activity to `scraper.log`
- supervisor script ensures continuous operation

## notes

- the script will continue running until a spot becomes available
- you can modify the check interval by changing the `time.sleep()` value in the script
- all errors and activities are logged to `scraper.log` for debugging purposes
- notifications can be received on both your phone and laptop through discord
- if the script crashes, it will automatically restart after 5 seconds
