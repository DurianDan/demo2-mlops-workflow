from .phase_1 import FraudDetection, CreditRiskPrediction, Predictor
from ..problem.schema import ResponseSchema, RequestSchema

import random
from abc import ABC, abstractmethod, abstractproperty
from typing import Dict


class MockPredictor:
    def __init__(self, raw_data: RequestSchema):
        self.raw_data = raw_data

    def predict(self) -> ResponseSchema:
        return ResponseSchema(
            id=self.raw_data.id,
            prediction=[random.choice([1, 0]) for _ in range(len(self.raw_data.rows))],
            drift=True,
        )


class PredictorFactory(ABC):
    @abstractproperty
    def predictor_idx(cls) -> Dict[int, Predictor]:
        return

    @abstractmethod
    def get_predictor(cls, prob_id: int) -> Predictor:
        ...


class Phase1PredictorFactory(PredictorFactory):
    predictor_idx = {1: FraudDetection, 2: CreditRiskPrediction}

    def get_predictor(self, prob_id: int) -> Predictor:
        return self.predictor_idx[prob_id]


class MockPredictorFactory(PredictorFactory):
    predictor_idx = {1: MockPredictor}

    def get_predictor(self, prob_id) -> Predictor:
        return self.predictor_idx[1]


class PredictorFactoryManager:
    factory_idx = {0: MockPredictorFactory, 1: Phase1PredictorFactory}

    @classmethod
    def get_factory(cls, phase_id: int) -> PredictorFactory:
        return cls.factory_idx[phase_id]

    @classmethod
    def get_predictor(cls, phase_id: int, prob_id: int) -> Predictor:
        factory = cls.factory_idx[phase_id]
        predictor = factory().get_predictor(prob_id)
        return predictor


if __name__ == "__main__":
    print(PredictorFactoryManager.get_predictor(1, 2))
