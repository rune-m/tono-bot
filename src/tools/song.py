from datetime import datetime
from typing import Tuple, List

class Song:
  def __init__(
    self,
    id: str,
    title: str,
    author: str,
    ccli: int,
    length: Tuple[int, int]
  ):
    self.id = id
    self.title = title if title is not None else "Ukjent"
    self.author = author if author is not None else "Ukjent"
    self.ccli = ccli
    self.length = length

  def __str__(self):
    return f'Id: {self.id} \
           \nTitle: {self.title} \
           \nAuthor: {self.author} \
           \nCCLI: {self.ccli} \
           \nLength: {self.length[0]}:{self.length[1]}\n'

class SongsWithDate:
  def __init__(self, songs: List[Song], date: datetime):
    self.songs = songs
    self.date = date