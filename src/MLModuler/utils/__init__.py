import pickle
import sys
import os
from src.MLModuler.exception import MyException
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

def save_object(file_path, obj):
  try:
    dir_path = os.path.dirname(file_path)

    os.makedirs(dir_path, exist_ok=True)

    with open(file_path, "wb") as file_obj:
      pickle.dump(obj, file_obj)

  except Exception as e:
    raise MyException(e, sys)
  

def model_evaluate(X_train, y_train, X_test, y_test, models, params):
  try:
    report = {}

    for i in range(len(list(models))):
      model = list(models.values())[i]
      para = list(params.values())[i]

      gv = GridSearchCV(model, para, cv=3, verbose=1, n_jobs=-1)
      gv.fit(X_train, y_train)

      model.set_params(**gv.best_params_)
      model.fit(X_train, y_train)

      y_train_predict = model.predict(X_train)

      y_test_predict = model.predict(X_test)

      train_model_r2_score = r2_score(y_train, y_train_predict)
      test_model_r2_score = r2_score(y_test, y_test_predict)

      report[list(models.keys())[i]] = test_model_r2_score

      return report





  except Exception as e:
    raise MyException(e, sys)