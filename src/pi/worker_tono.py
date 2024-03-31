#!/usr/bin/python3
import schedule
import time
from datetime import datetime
from main_pi import run
    
schedule.every().monday.at("03:00").do(run)

print(str(datetime.now()) + " - Starter TonoBot...")

while 1:
    try:
        schedule.run_pending()
        time.sleep(1)
    except:
        print(str(datetime.now()) + " - Error occured!")