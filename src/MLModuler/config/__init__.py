from dataclasses import dataclass
import os

@dataclass
class DataIngestionConfig:
  train_data_path = os.path.join("artifact", "train.csv")
  test_data_path = os.path.join("artifact", "test.csv")
  raw_data_path = os.path.join("artifact", "raw.csv")
