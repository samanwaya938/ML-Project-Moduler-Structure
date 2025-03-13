from dataclasses import dataclass
import os

@dataclass
class DataIngestionConfig:
  train_data_path = os.path.join("artifact","Data_Ingestion", "train.csv")
  test_data_path = os.path.join("artifact", "Data_Ingestion", "test.csv")
  raw_data_path = os.path.join("artifact", "Data_Ingestion", "raw.csv")

@dataclass
class DataTransformationConfig:
  transformation_data_path = os.path.join("artifact", "Data_Transformation", "prepossessor.pkl")


@dataclass
class ModelTrainerConfig:
  model_trainer_path = os.path.join("artifact", "Model trainer", "model.pkl")