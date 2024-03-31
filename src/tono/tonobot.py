from selenium import webdriver
from tono.tono_scraper import fyllInnDatoOgKlokkeslett, fyllInnInfo, fyllInnSang, lagreFremforing, leggTilSangfelt, loggInnToTono, navigerTilFremforing, openTono, sendFremforing
from tools.song import SongsWithDate

def sendSongsToTono(driver: webdriver.Chrome, songsWithDate: SongsWithDate):
  songs = songsWithDate.songs

  openTono(driver)
  navigerTilFremforing(driver)
  fyllInnDatoOgKlokkeslett(driver, songsWithDate.date)
  leggTilSangfelt(driver, len(songs))

  songsWithUnkownArtist = []
  for i in range(len(songs)):
    song = songs[i]
    if song.author == 'Ukjent':
      songsWithUnkownArtist.append(song.title)
    fyllInnSang(driver, i + 1, song)
  fyllInnInfo(driver)
  lagreFremforing(driver)
  # sendFremforing(driver)

  return songsWithUnkownArtist
