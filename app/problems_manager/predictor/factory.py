from ..base_factory import BaseFactory
from .base import BasePredictor


class PredictorFactory(BaseFactory):
    
    
    def get_predictor(self) -> BasePredictor:
        pass