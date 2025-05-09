import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

def send_test_notification():
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
    
    # Create Discord embed
    embed = {
        "title": "🎓 Test Notification",
        "description": "This is a test notification for the CS 7650 course availability checker!\n\nIf you see this, the notifications are working correctly.",
        "color": 5814783,  # Blue color
        "timestamp": datetime.utcnow().isoformat()
    }
    
    # Send to Discord
    payload = {
        "embeds": [embed]
    }
    
    try:
        response = requests.post(
            webhook_url,
            json=payload
        )
        response.raise_for_status()
        print("Test notification sent successfully!")
    except Exception as e:
        print(f"Failed to send notification: {e}")

if __name__ == "__main__":
    send_test_notification() 