import threading
from loguru import logger

logger.add("/var/log/python_{time:YYYY-MM-DD_HH-mm-ss}.log", rotation="500 MB", retention="10 days", compression="zip", serialize=True)

def job():
    logger.info('Job started')
    threading.Timer(5, job).start()
threading.Timer(5, job).start()

