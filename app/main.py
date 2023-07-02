from .predictor import PredictorFactoryManager
from .problem.schema import ResponseSchema, RequestSchema, MockResponseSchema
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.post("/phase-{phase_id}/prob-{prob_id}/predict")
async def predict_handler(
    phase_id: int, prob_id: int, content: RequestSchema
) -> ResponseSchema:
    PredictorClass = PredictorFactoryManager().get_predictor(
        phase_id, prob_id
    )
    predictor = PredictorClass(content)
    return predictor.predict()


@app.post("/test/phase-{phase_id}/prob-{prob_id}/predict")
async def test_predict_handler(
    phase_id: int, prob_id: int, content: RequestSchema
) -> MockResponseSchema:
    PredictorClass = PredictorFactoryManager().get_predictor(
        0, prob_id
    )
    predictor = PredictorClass(content)
    return MockResponseSchema(
        id=content.id,
        message=f"testing api with mock result, phase {phase_id}, problem {prob_id}, at {datetime.now().astimezone()}",
        response_body=predictor.predict()
    )


@app.get("/")
def hello():
    return {"Hello":"World"}