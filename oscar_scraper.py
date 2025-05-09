import requests
from bs4 import BeautifulSoup
import time
from plyer import notification
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)

class OscarScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def check_availability(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            reg_section = soup.find(string='Registration Availability')
            if reg_section:
                reg_table = reg_section.find_parent('table')
                if reg_table:
                    rows = reg_table.find_all('tr')
                    for row in rows:
                        cells = row.find_all('td')
                        if len(cells) == 3: 
                            try:
                                capacity = int(cells[0].text.strip())
                                actual = int(cells[1].text.strip())
                                remaining = int(cells[2].text.strip())
                                logging.info(f"Found seat information - Capacity: {capacity}, Actual: {actual}, Remaining: {remaining}")
                                return actual, capacity
                            except (ValueError, IndexError) as e:
                                logging.error(f"Error parsing numbers: {e}")
                                continue
            
            logging.error("Could not find seat information in the expected format")
            return None

        except requests.RequestException as e:
            logging.error(f"Error making request: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return None

    def send_notification(self, enrolled, capacity):
        title = "Course Spot Available!"
        message = f"A spot has opened up! Current enrollment: {enrolled}/{capacity}"
        
        try:
            notification.notify(
                title=title,
                message=message,
                app_icon=None,
                timeout=10,
            )
            logging.info("Notification sent successfully")
        except Exception as e:
            logging.error(f"Failed to send notification: {e}")

def main():
    url = "https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_detail_sched?term_in=202505&crn_in=57752"
    scraper = OscarScraper(url)
    
    logging.info("Starting course availability checker...")
    logging.info(f"Monitoring URL: {url}")
    
    try:
        while True:
            result = scraper.check_availability()
            
            if result:
                enrolled, capacity = result
                remaining = capacity - enrolled
                logging.info(f"Current status - Enrolled: {enrolled}/{capacity}, Remaining: {remaining}")
                
                if remaining > 0:
                    logging.info("Spot available! Sending notification...")
                    scraper.send_notification(enrolled, capacity)
                    break
            else:
                logging.warning("Failed to get enrollment information, will retry in 5 minutes")
            
            logging.info("Waiting 5 minutes before next check...")
            time.sleep(300)
    
    except KeyboardInterrupt:
        logging.info("Scraper stopped by user")
    except Exception as e:
        logging.error(f"Unexpected error in main loop: {e}")

if __name__ == "__main__":
    main() 