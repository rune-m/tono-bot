from datetime import datetime
import dateutil.parser
import datetime as dt
from typing import Tuple, List
import pytz
from enum import Enum

def secondsToMinSec(seconds: int) -> Tuple[int, int]:
  min = seconds // 60
  sec = seconds % 60
  return (min, sec)

def parseStrToDate(dateStr: str):
  return dateutil.parser.isoparse(dateStr)

def dateHasPassed(isoDateTime: str) -> bool:
  todayTimestamp = datetime.today().timestamp()
  inputTimestamp = dateutil.parser.isoparse(isoDateTime).timestamp()
  return inputTimestamp <= todayTimestamp

def beautifyDateTime(isoDateTime: str) -> str:
  return dateutil.parser.isoparse(isoDateTime).strftime("%d.%m.%Y %H:%M")

def formatLog(text: str):
  return text.replace("\n", "<br />- ")[0:-2]

def removeIkkeBestemtSang(planItemsData: dict, songs: List) -> List:
  '''
  Removes potential "Ikke bestemt sang" from the list of songs
  '''
  return list(filter(lambda song: "ikke bestemt sang" not in song["attributes"]["title"].lower(), songs))

def dateIsWithinLast7Days(dateStr: str):
  utc=pytz.UTC
  date = parseStrToDate(dateStr).replace(tzinfo=utc)
  today = datetime.today().replace(tzinfo=utc)
  weekAgo = today - dt.timedelta(days=7)
  return date > weekAgo and date < today

class Status(Enum):
    SUCCESS = 1
    ERROR = 2
