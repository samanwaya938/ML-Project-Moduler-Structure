import os
import sys
from src.MLModuler.logger import logging
from src.MLModuler.exception import MyException
from src.MLModuler.config import DataTransformationConfig
from src.MLModuler.utils import save_object
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd




class DataTransformation:
  def __init__(self):
    self.data_transformation_config = DataTransformationConfig()

  def get_data_transformer_object(self):
    try:
      numeric_colums = ['reading_score', 'writing_score']
      categorical_colums = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

      num_pipline = Pipeline(
        steps=[
          ('imputer', SimpleImputer(strategy='median')),
          ('scaler', StandardScaler(with_mean=False))
        ]
      )

      cat_pipleline = Pipeline(      
        steps=[
          ('imputer', SimpleImputer(strategy='most_frequent')),
          ('one_hot_encoder', OneHotEncoder()),
          ('scaler', StandardScaler(with_mean=False))
        ]
      )

      logging.info(f"Numerical columns: {numeric_colums}")
      logging.info(f"Categorical columns: {categorical_colums}")
      
      preprocessor = ColumnTransformer(
        [
          ('num_pipline', num_pipline, numeric_colums),
          ('cat_pipleline', cat_pipleline, categorical_colums)
        ]
      )

      return preprocessor
    
    except Exception as e:
      raise MyException(e, sys)
    
  def initiate_data_transformation(self, train_path, test_path):
    try:
      train_df = pd.read_csv(train_path)
      test_df = pd.read_csv(test_path)

      preprocessor_obj = self.get_data_transformer_object()

      target_column = 'math_score'
      numerical_columns = ['reading_score', 'writing_score']

      logging.info(f"Train and test data read ")

      input_feature_train_df = train_df.drop(target_column, axis=1)
      target_feature_train_df = train_df[target_column]

      input_feature_test_df = test_df.drop(target_column, axis=1)
      targer_feature_test_df = test_df[target_column]

      logging.info(f"Applying preprocessing object on training dataframe and testing dataframe.")

      input_feature_train_df_arr = preprocessor_obj.fit_transform(input_feature_train_df)
      input_feature_test_df_arr = preprocessor_obj.transform(input_feature_test_df)

      train_arr = np.c_[input_feature_train_df_arr, np.array(target_feature_train_df)]
      test_arr = np.c_[input_feature_test_df_arr, np.array(targer_feature_test_df)]

      logging.info(f"Saved preprocessing object.")

      save_object(
        file_path=self.data_transformation_config.transformation_data_path,
        obj=preprocessor_obj
      )

      return(
        train_arr,
        test_arr,
        self.data_transformation_config.transformation_data_path
      )
  

    except Exception as e:
      raise MyException(e, sys)  