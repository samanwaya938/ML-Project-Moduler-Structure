import sys
from src.MLModuler.logger import logging
from src.MLModuler.exception import MyException
from src.MLModuler.components.data_ingestion import DataIngestion
from src.MLModuler.components.data_transformation import DataTransformation

"__name__" == "__main__"
logging.info("logging has started")

try:
  data_ingestion = DataIngestion()
  train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

  data_transformation = DataTransformation()
  data_transformation.initiate_data_transformation(train_data_path, test_data_path)
except Exception as e:
  raise MyException(e, sys)