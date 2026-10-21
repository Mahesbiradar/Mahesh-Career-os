"""1. Application logging system
Easy–Medium
10 marks

Create `app_logger.py`. Configure a named logger with timestamps, severity, and message. 
Log application startup at INFO, an invalid input at WARNING, and a simulated exception with its traceback. 
Write logs to a file. Do not log secrets.

"""

import logging


logging.basicConfig(filename="logging.log", level=logging.DEBUG, format= "%(asctime)s | %(levelname)s | %(name)s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

logger = logging.getLogger(__name__)


logger.info("Application started")

logger.warning("Invalid Input")

try:

    num = 4/0

except ZeroDivisionError as e:

    logger.exception(f"Invalid operations the error is : {e}")








