import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bot import run_bot

driverLoader = lambda: webdriver.Chrome(service=Service(ChromeDriverManager().install()))

run_bot(driverLoader)
# run_bot(driverLoader, datetime.datetime(2024, 2, 20))
