import datetime
from selenium import webdriver
from bot import run_bot

driverLoader = lambda: webdriver.Chrome()

print("Kjører TonoBot...")

# run_bot(driverLoader)
run_bot(driverLoader, datetime.datetime(2025, 3, 17))
