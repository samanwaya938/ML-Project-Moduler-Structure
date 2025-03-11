import os
import sys
from src.MLModuler.logger import logging
from src.MLModuler.exception import CustomException
import numpy as np
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
  transformation_data_path = os.path.join("artifact", "prepossessor.pkl")