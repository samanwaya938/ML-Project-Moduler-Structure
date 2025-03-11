from dataclasses import dataclass
import os

@dataclass
class DataIngestionConfig:
  train_data_path = os.path.join("artifact","Data_Ingestion", "train.csv")
  test_data_path = os.path.join("artifact", "Data_Ingestion", "test.csv")
  raw_data_path = os.path.join("artifact", "Data_Ingestion", "raw.csv")
