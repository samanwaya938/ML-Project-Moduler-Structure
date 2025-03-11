import os
import sys
import logging
from datetime import datetime

FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_dir, FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
  filemode="w",
  format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
  level=logging.INFO

)

