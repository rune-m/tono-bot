from datetime import datetime
from tools.song import Song, SongsWithDate
from tools.api_client import getFromApi, getFromUrl
from tools.utils import beautifyDateTime, dateHasPassed, dateIsWithinLast7Days, parseStrToDate, removeIkkeBestemtSang, secondsToMinSec
from tools.logger import Logger
from constants import PCO_APP_ID, PCO_SECRET
import base64

HOSTNAME = "https://api.planningcenteronline.com/services/v2"

basic_auth_string = f'{PCO_APP_ID}:{PCO_SECRET}'
b64auth = base64.b64encode(basic_auth_string.encode("UTF-8"))

def getLastSundayPlans(numberOfSundays=1, onlyCheckLast7Days=False):
  # Get last 100 plans and find the last completed plan
  Logger.log("Henter planer...")
  try:
    plans = getFromApi(f'{HOSTNAME}/service_types/631909/plans?order=-sort_date&per_page=100', auth_token=f'Basic {b64auth.decode("UTF-8")}')
  except:
    raise Exception("Kunne ikke hente planer fra PCO")
  sundays = []
  for plan in iter(plans["data"]):
    if numberOfSundays <= 0:
      break
    planDateStr = plan["attributes"]["sort_date"];
    if dateHasPassed(planDateStr):
      if (not onlyCheckLast7Days or dateIsWithinLast7Days(planDateStr)):
        sundays.append(plan)
        numberOfSundays -= 1
  return sundays

def getAllSundaysFromDate(fromDateInclusive: datetime):
  Logger.log("Hener planer...")
  try:
    plans = getFromApi(f'{HOSTNAME}/service_types/631909/plans?order=-sort_date&per_page=100', auth_token=f'Basic {b64auth.decode("UTF-8")}')
  except:
    raise Exception("Kunne ikke hente planer fra PCO")
  sundays = []
  today = datetime.today()
  # today = datetime.today() - timedelta(days=2) # Foreløpig
  for plan in iter(plans["data"]):
    planDate = parseStrToDate(plan["attributes"]["sort_date"])
    if planDate.timestamp() >= fromDateInclusive.timestamp() and planDate.timestamp() <= today.timestamp():
      sundays.append(plan)
  return sundays

def getSongsFromPlan(plan):
  # Fetch the plan
  Logger.log(f'Henter sanger fra plan ({beautifyDateTime(plan["attributes"]["sort_date"])})...')
  try:
    planItems = getFromUrl(plan["links"]["self"] + "/items?include=song,arrangement&per_page=100", auth_token=f'Basic {b64auth.decode("UTF-8")}')
  except:
    raise Exception("Kunne ikke hente sanger fra plan")

  # Find all songs and arrangements in plan
  songs = list(filter(lambda item: item["type"] == "Song", planItems["included"]))
  arrangements = list(filter(lambda item: item["type"] == "Arrangement", planItems["included"]))

  # Remove potential IKKE BESTEMT SANG
  songs = removeIkkeBestemtSang(planItems["data"], songs)

  # Join songs with arrangement length
  for song in songs:
    for arrangement in arrangements:
      if arrangement["relationships"]["song"]["data"]["id"] == song["id"]:
        song["attributes"]["length"] = arrangement["attributes"]["length"]

  mappedSongs = list(
    map(
      lambda song:
        Song(
          song["id"],
          song["attributes"]["title"],
          song["attributes"]["author"],
          song["attributes"]["ccli_number"],
          secondsToMinSec(song["attributes"]["length"]) if "length" in song["attributes"] else None
        ), 
      songs
    ))

  parsedDate = parseStrToDate(plan["attributes"]["sort_date"])

  return SongsWithDate(mappedSongs, parsedDate)
