from typing import Any, Dict, Sequence

from ..problem.schema import RequestSchema, ResponseSchema
from .abstract import Predictor


class FraudDetection(Predictor):
    def __init__(self, raw_data: RequestSchema) -> None:
        super().__init__(raw_data)

    def load_model(self):
        ...

    def predict(self) -> ResponseSchema:
        ...


class CreditRiskPrediction(Predictor):
    def __init__(self, raw_data: RequestSchema) -> None:
        super().__init__(raw_data)

    def load_model(self):
        ...

    def predict(self) -> ResponseSchema:
        ...
