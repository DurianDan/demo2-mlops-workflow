from ..base_factory import BaseFactory
from .base import BasePredictor
from .model_manager import ModelManager
from typing import Type, Literal
import importlib


class PredictorFactory(BaseFactory):
    def get_predictor_type(self) -> Type[BasePredictor]:
        module_import_path = (
            f"app.problems_manager.predictor.phase{self.phase_id}"
        )
        predictor_name = f"Prob{self.prob_id}Predictor"
        return getattr(
            importlib.import_module(module_import_path), predictor_name
        )

    def get_predictor(
        self, model_version: Literal["production", "development"] | int
    ) -> BasePredictor:
        predictor_type = self.get_predictor_type()
        return predictor_type(model_version)
