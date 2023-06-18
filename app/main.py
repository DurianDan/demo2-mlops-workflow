from fastapi import FastAPI
import random
import mlflow
from typing import Any, Union

from .db import engine, session_local
from .problem.api_models.factory import ModelCreator
from .problem.api_models import Base
from .problem.schema import RequestSchema, ResponseSchema
from .predict import test_model_from_judges
import pandas as pd

Base.metadata.create_all(bind=engine)
app = FastAPI()
model_creator = ModelCreator()


@app.get("/")
def read_root():
    return {"Hello": "World"}

from pathlib import Path

@app.post("/phase-{phase_id}/prob-{prob_id}/predict")
async def recieve(phase_id: int, prob_id: int, request_data: RequestSchema) -> Union[ResponseSchema, Any]:
    # session = session_local()
    # api_model = model_creator.create_model(phase_id, prob_id)
    all_records = []

    for info in request_data.rows:
        # add each record to the db
        record = {
            col_name: info[idx]
            for idx, col_name in enumerate(request_data.columns)
        }
        all_records.append(record)
        # session.add(api_model(**record, request_id=request_data.id))
        # session.commit()

    model_path= "/code/app/mlflow/data/mlartifacts/1/3128571ecd3242cfae5d2b771dcc7b84/artifacts/model"
    
    result = None
    try:
        data=pd.DataFrame(all_records)
        data["feature2"] = data["feature2"].astype("int32")
        data["feature1"] = data["feature1"].astype("int32")

        loaded_model = mlflow.pyfunc.load_model(model_path)
        prediction = loaded_model.predict(data)
        drift = random.choice([0, 1])

        result = {
            "predictions": prediction.tolist(),
            "drift": int(drift),
            "id": int(request_data.id)
        }

    except Exception as err : 
        result = { "error" : str(err)}
    
    return result

@app.post("/test")
def load_model(request_data: RequestSchema):
    all_records = []

    for info in request_data.rows:
        record = {
            col_name: info[idx]
            for idx, col_name in enumerate(request_data.columns)
        }
        all_records.append(record)

    model_path= "/code/app/mlflow/data/mlartifacts/1/3128571ecd3242cfae5d2b771dcc7b84/artifacts/model"
    
    result = None
    try:
        data=pd.DataFrame(all_records)
        data["feature2"] = data["feature2"].astype("int32")
        data["feature1"] = data["feature1"].astype("int32")

        loaded_model = mlflow.pyfunc.load_model(model_path)
        prediction = loaded_model.predict(data)
        drift = random.choice([0, 1])

        result = {
            "predictions": prediction,
            "drift": int(drift),
            "id": int(request_data.id),
            "model": type(prediction)
        }

    except Exception as err : 
        result = { "error" : str(err) }
    try:
        return result
    except Exception as err: 
        return {
            "model": str(type(prediction)),
            "error": str(err)
        }
            