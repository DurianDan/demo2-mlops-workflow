from abc import ABC, abstractmethod
from typing import Sequence, Dict, Any
from pydantic import BaseModel
from ..problem.schema import RequestSchema, ResponseSchema


class Predictor(ABC):
    def __init__(self, raw_data: RequestSchema) -> None:
        self.raw_data = raw_data

    @abstractmethod
    def load_model(self):
        ...

    @abstractmethod
    def predict(self) -> ResponseSchema:
        ...
