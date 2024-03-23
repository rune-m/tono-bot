from imp import reload
import logging
from io import StringIO
from datetime import datetime
import os

class Logger:
  __log_stream = StringIO()
  ERROR = logging.ERROR

  def setUpLogger():
    logging.shutdown()
    reload(logging)

    if not os.path.exists(f'src/logs'):
      os.makedirs(f'src/logs')

    Logger.__log_stream = StringIO()
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO,
                        datefmt='%d %b %y %H:%M:%S',
                        handlers=[
                          logging.StreamHandler(),
                          logging.FileHandler(f'{__file__}/../../logs/{datetime.now().strftime("%Y%m%d_%H-%M_log")}'),
                          logging.StreamHandler(Logger.__log_stream)
                        ])

  def log(msg, level=logging.INFO):
    logger = logging.getLogger(__name__)
    logger.log(msg=msg, level=level)

  def getLog():
    return Logger.__log_stream.getvalue()
