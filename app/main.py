from fastapi import FastAPI
import mlflow
from os import getenv

from .schemas import RequestSchema, ResponseSchema
from .problems_manager import ProblemsManager


app = FastAPI()


@app.post("/phase-{phase_id}/prob-{prob_id}/predict")
def problems_handler(
    phase_id: int, prob_id: int, request_body: RequestSchema
) -> ResponseSchema:
    manager = ProblemsManager(
        prob_id=prob_id,
        phase_id=phase_id,
        ml_model_version="production",
        request_body=request_body,
    )
    predictor, sql_model = manager.get_products()
    predictor.predict(request_body.get_frame())
    # TODO: saving data to sql model
    # sql_model
