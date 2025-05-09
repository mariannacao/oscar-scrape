# oscar course availability checker

this script monitors a specific course in georgia tech's oscar system and notifies you via discord when a spot becomes available. it runs on a server using crontab for efficient scheduling.

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

to run the script once on your local machine:
```bash
python oscar_scraper.py
```

## running on server

the script is configured to run on a server using crontab to check every 5 minutes. to deploy to your own server:

1. set up a server:
   - you can use any linux server (aws ec2, digitalocean, linode, etc.)
   - make sure you have ssh access to the server
   - note down your server's ip address and ssh port

2. prepare deployment:
   - copy `deploy.sh.example` to `deploy.sh.local`
   - update the server details in `deploy.sh.local`:
     ```bash
     SERVER="your-username@your-server-ip"
     PORT="your-ssh-port"  # usually 22
     ```

3. run the deployment script:
```bash
chmod +x deploy.sh.local
./deploy.sh.local
```

the deployment script will:
- copy all necessary files to the server
- set up a python virtual environment
- install required dependencies
- set up crontab to run the script every 5 minutes
- test the discord notification

## monitoring

to check the status of the scraper on your server:

```bash
# check if crontab is running
ssh -p $PORT $SERVER "crontab -l"

# check recent logs
ssh -p $PORT $SERVER "tail -f ~/oscar-scraper/scraper.log"

# check last 20 log entries
ssh -p $PORT $SERVER "tail -n 20 ~/oscar-scraper/scraper.log"
```

## stopping the script

to stop the script from running:
```bash
# remove the crontab entry
ssh -p $PORT $SERVER "crontab -l | grep -v 'oscar_scraper.py' | crontab -"
```

## features

- checks course availability every 5 minutes using crontab
- sends discord notifications when a spot opens up
- notifications include:
  - current enrollment status
  - number of remaining spots
  - direct link to register
  - timestamp
- runs efficiently using crontab scheduling
- logs all activity to `scraper.log`
- automatically restarts after server reboots (thanks to crontab)

## notes

- the script checks availability every 5 minutes
- all errors and activities are logged to `scraper.log` for debugging purposes
- notifications can be received on both your phone and laptop through discord
- the script will continue running until you remove it from crontab
- crontab ensures the script runs even after server restarts
- you'll need your own server to run this continuously

## modifying check interval

to change how often the script checks for availability:
1. ssh into your server
2. edit the crontab:
   ```bash
   ssh -p $PORT $SERVER "crontab -e"
   ```
3. modify the timing in the crontab entry:
   - `*/5 * * * *` = every 5 minutes
   - `*/10 * * * *` = every 10 minutes
   - `*/1 * * * *` = every minute
   - etc.
