from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tools.song import Song
from tools.logger import Logger
from constants import TONO_MAIL, TONO_PASSWORD, CHURCH_INFO as info

def loggInnToTono(driver: webdriver.Chrome):
  try:
    Logger.log("Logger inn hos Tono...")
    driver.get('https://m.tono.no/Login/')

    userElem = driver.find_element(By.XPATH, '//*[@id="inputUsername"]')
    userElem.send_keys(TONO_MAIL)

    Neste = driver.find_element(By.NAME, 'login')
    Neste.click()

    passwordElem = driver.find_element(By.XPATH, '//*[@id="inputPassword"]')
    passwordElem.send_keys(TONO_PASSWORD) 

    loggInn = driver.find_element(By.XPATH, '//*[@id="loginform"]/div[3]/button')
    loggInn.click()

  except:
    raise Exception("Kunne ikke logge inn hos Tono")

def navigerTilFremforing(driver: webdriver.Chrome):
  try:
    seremoniKnapp = driver.find_element(By.XPATH, '/html/body/div/aside/div/div[4]/div/div/nav/ul/li[1]/a')
    driver.execute_script("arguments[0].click();", seremoniKnapp)

    fremforingKnapp = driver.find_element(By.XPATH, '//*[@id="itemid_280"]')
    driver.execute_script("arguments[0].click();", fremforingKnapp)
  except:
    raise Exception("Kunne ikke navigere til fremføring")

def fyllInnDatoOgKlokkeslett(driver: webdriver.Chrome, date: datetime):
  try:
    Logger.log("Fyller ut dato og klokkeslett...")
    datoInput = driver.find_element(By.XPATH, '//*[@id="startDate"]')
    datoInput.send_keys(f'{date.day}.{date.month}.{date.year}')
    datoInput.send_keys(Keys.RETURN)

    klokkeInput = driver.find_element(By.XPATH, '//*[@id="time"]')
    klokkeInput.send_keys('12:00')
    klokkeInput.send_keys(Keys.RETURN)
  except:
    raise Exception("Kunne ikke fylle inn dato og klokkeslett")

def leggTilSangfelt(driver: webdriver.Chrome, antallSanger):
  try:
    Logger.log("Legger til ekstra sangfelter...")
    leggTilKnapp = driver.find_element(By.XPATH, '//*[@id="more_fields"]')
    antallKlikk = antallSanger - 4 if antallSanger - 4 >= 0 else 0
    for i in range(antallKlikk):
      leggTilKnapp.click()
  except:
    raise Exception("Kunne ikke legge til ekstra sangfelter")

def fyllInnSang(driver: webdriver.Chrome, index, song: Song):
  try:
    Logger.log(f'Legger til {song.title} hos Tono...')
    tittelInput = driver.find_element(By.XPATH, f'//*[@id="workTitle{index}"]')
    tittelInput.send_keys(song.title)
    rettighetsInput = driver.find_element(By.XPATH, f'//*[@id="workComposer{index}"]')
    rettighetsInput.send_keys(song.author)
    if song.length != None:
      minutterInput = driver.find_element(By.XPATH, f'//*[@id="workPerformanceMins{index}"]')
      minutterInput.send_keys(song.length[0])
      sekunderInput = driver.find_element(By.XPATH, f'//*[@id="workPerformanceSecs{index}"]')
      sekunderInput.send_keys(song.length[1])
  except:
    raise Exception(f'Kunne ikke legge til sang: {song.title}')

def fyllInnInfo(driver: webdriver.Chrome):
  try:
    Logger.log("Fyller ut info om lokale...")
    navnInput = driver.find_element(By.XPATH, '//*[@id="venName"]')
    navnInput.send_keys(info['navn'])
    adresseInput = driver.find_element(By.XPATH, '//*[@id="venAddress"]')
    adresseInput.send_keys(info['adresse'])
    postnummerInput = driver.find_element(By.XPATH, '//*[@id="venPostCode"]')
    postnummerInput.send_keys(info['postnummer'])
    poststed = driver.find_element(By.XPATH, '//*[@id="venCity"]')
    poststed.send_keys(info['poststed'])
    for i in range(6): poststed.send_keys(Keys.BACKSPACE)
    tlfInput = driver.find_element(By.XPATH, '//*[@id="venPhone"]')
    tlfInput.send_keys(info['tlf'])
    hjemmesideInput = driver.find_element(By.XPATH, '//*[@id="venWww"]')
    hjemmesideInput.send_keys(info['hjemmeside'])
  except:
    raise Exception("Kunne ikke fylle inn info om lokale")

def lagreFremforing(driver: webdriver.Chrome):
  try:
    Logger.log("Lagrer fremføring...")
    lagreKnapp = driver.find_element(By.XPATH, '//*[@id="btnSave"]')
    driver.execute_script("arguments[0].click();", lagreKnapp)
  except:
    raise Exception("Kunne ikke lagre fremføring")

def sendFremforing(driver: webdriver.Chrome):
  try:
    Logger.log("Sender fremføring til Tono...")
    sendKnapp = driver.find_element(By.XPATH, '//*[@id="btnSend"]')
    driver.execute_script("arguments[0].click();", sendKnapp)
    sleep(3)
  except:
    raise Exception("Kunne ikke sende fremføring til Tono")

def openTono(driver: webdriver.Chrome):
  try:
    Logger.log("Navigerer til Tono...")
    driver.get("https://m.tono.no")
  except Exception as e:
    raise Exception("Kunne ikke navigere til Tono", e)