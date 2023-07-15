from abc import ABC, abstractmethod
from pandas import DataFrame
from numpy import ndarray
from typing import List, Any
from ...schemas import ResponseSchema
from .model_manager import ModelManager


class BasePredictor(ABC):
    def __init__(self, model_manager: ModelManager):
        self.model = model_manager.get_model()
        self.model_manager = model_manager

    @abstractmethod
    def predict(
        self, data: DataFrame | ndarray | List[List[Any]]
    ) -> ResponseSchema:
        """
        Get predictions from the loaded model
        """
        ...
