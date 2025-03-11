import sys
from src.MLModuler.logger import logging
from src.MLModuler.exception import MyException
from src.MLModuler.components.data_ingestion import DataIngestion

"__name__" == "__main__"
logging.info("logging has started")

try:
  data_ingestion = DataIngestion()
  data_ingestion.initiate_data_ingestion()
except Exception as e:
  raise MyException(e, sys)