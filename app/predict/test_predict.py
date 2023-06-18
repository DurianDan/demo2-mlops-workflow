import mlflow
import random
from pandas import DataFrame

def test_model_from_judges(data: DataFrame, model_path: str):
    '''
    Phase1
    Prob1
    '''
    data["feature2"] = data["feature2"].astype("category")
    data["feature1"] = data["feature1"].astype("category")
    loaded_model = mlflow.pyfunc.load_model(model_path)
    prediction = loaded_model.predict(loaded_model)
    drift = random.choice([0, 1])

    return {
        "predictions": prediction,
        "drift": drift
    }