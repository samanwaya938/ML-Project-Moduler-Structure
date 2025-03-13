import pandas as pd
import os
import sys
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from src.MLModuler.config import ModelTrainerConfig
from src.MLModuler.exception import MyException
from src.MLModuler.logger import logging
from src.MLModuler.utils import model_evaluate, save_object




class ModelTrainer:
  def __init__(self):
    self.model_trainer_config = ModelTrainerConfig()

  def initiate_model_trainer(self, train_array, test_array):
    try:
      logging.info("Splitting training and test input and target feature")
      X_train, y_train, X_test, y_test = (
        train_array[:, :-1],
        train_array[:, -1],
        test_array[:,:-1],
        test_array[:,-1]
      )


      logging.info("Model training started")
      models = {
        "Decision Tree ":DecisionTreeRegressor(),
        "Random Forest":RandomForestRegressor()
      }

      params = {
        "Decision Tree":{
          "criterion":["squared_error", "friedman_mse", "absolute_error"],
          "splitter":["best", "random"],
          "max_features":["sqrt", "log2"]
        },
        "Random Forest":{
          "criterion":["squared_error", "friedman_mse", "absolute_error"],
          "max_features":["sqrt", "log2"],
          "n_estimators":[8,16,32,64,128,256],
          "max_depth":[50,100]

        }
      }
      
      model_report:dict = model_evaluate(X_train, y_train, X_test, y_test, models, params)

      best_model_score = max(sorted(model_report.values()))

      best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

      best_model = models[best_model_name]

      if best_model_score<0.2:
        raise Exception("No best model found")

      logging.info(f"Best model found on both training and testing dataset")

      save_object(
        file_path=self.model_trainer_config.model_trainer_path,
        obj=best_model
      )

      predicted=best_model.predict(X_test)

      predicted_r2_score = r2_score(y_test, predicted)

      return predicted_r2_score

       
    except Exception as e:
      raise MyException(e, sys)