from tono.tonobot import run_bot
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

display = Display(visible=0, size=(1600, 1600))
display.start()

service = Service(f'/usr/lib/chromium-browser/chromedriver')
driverLoader = lambda: webdriver.Chrome(service=service)

run_bot(driverLoader)