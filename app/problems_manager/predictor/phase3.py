from typing import Any, List
from numpy import ndarray
from pandas import DataFrame

from .model_manager import ModelManager
from .base import BasePredictor


class Prob1Predictor(BasePredictor):
    def __init__(self, model_manager: ModelManager):
        super().__init__(model_manager)

    def predict(self, data: DataFrame | ndarray) -> List[Any]:
        return self.model_manager.resolve_prediction(self.model.predict(data))


class Prob2Predictor(BasePredictor):
    def __init__(self, model_manager: ModelManager):
        super().__init__(model_manager)

    def predict(self, data: DataFrame | ndarray) -> List[Any]:
        return self.model_manager.resolve_prediction(self.model.predict(data))
