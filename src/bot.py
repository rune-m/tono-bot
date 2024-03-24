from tono.tonobot import sendSongsToTono
from tools.logger import Logger
from tools.mail_client import send_email
from services.planning_center import getAllSundaysFromDate, getLastSundayPlans, getSongsFromPlan
from tono.tono_scraper import loggInnToTono
from tools.utils import formatLog
from constants import MAIL_TO_RECIEVE_STATUS_MAIL
from tools.utils import Status

def run_bot(driverLoader, fromDate=None):
  '''
  Kjør TonoBot. Henter planer fra Planning Center. Henter fra forrige møte hvis fromDate=None.

  Parameters
  - driverLoader - Loader for browser driveren som skal brukes
  - fromDate - Henter planer fra og med denne datoen (default=None)
  '''
  sendFromDate = fromDate != None

  Logger.setUpLogger()
  driver = driverLoader()

  loggInnToTono(driver)

  allSongsWithUnknownArtist = []
  allSongsWithoutCCLI = []

  try:
    plans = getAllSundaysFromDate(fromDate) if sendFromDate else getLastSundayPlans(numberOfSundays=1, onlyCheckLast7Days=True)

    for plan in plans:
      songsWithDate = getSongsFromPlan(plan)

      songsWithUnknownArtist = sendSongsToTono(driver, songsWithDate)
      allSongsWithUnknownArtist += songsWithUnknownArtist

    allSongsWithUnknownArtist = list(set(allSongsWithUnknownArtist))
    allSongsWithoutCCLI = list(set(allSongsWithoutCCLI))

    status = Status.SUCCESS
    Logger.log(status.value)

  except Exception as e:
    status = Status.ERROR
    Logger.log(f'Feilet: {e}', level=Logger.ERROR)
  finally:
    for mail in MAIL_TO_RECIEVE_STATUS_MAIL:
      send_email(mail, status, formatLog(Logger.getLog()), allSongsWithUnknownArtist, allSongsWithoutCCLI)
    Logger.log("Ferdig!\n")
