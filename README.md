# oscar course availability checker

monitors a specific course in georgia tech's oscar system and sends discord notifications when a spot opens up.

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

3. test notification:
```bash
python test_notification.py
```

## deployment

1. update server details in `deploy.sh.local`:
```bash
SERVER="your-username@your-server-ip"
```

2. deploy:
```bash
chmod +x deploy.sh.local
./deploy.sh.local
```

## monitoring

check logs:
```bash
ssh -p 2200 your-username@your-server-ip "tail -f ~/scraper.log"
```

## stopping the script

remove from crontab:
```bash
ssh -p 2200 your-username@your-server-ip "crontab -r"
```

## features

- checks every 5 minutes using crontab
- discord notifications when spots open
- automatic restart after server reboots
- all activity logged to `scraper.log`
