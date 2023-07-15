from mlflow.pyfunc import PyFuncModel, load_model, PyFuncOutput
from mlflow import set_tracking_uri
from pydantic import BaseModel

from os import getenv
from typing import Literal, List, Any
from pathlib import Path


set_tracking_uri(getenv("MLFLOW_SERVER_TRACKING_URI"))
ML_MODEL = PyFuncModel


class ModelManager(BaseModel):
    phase_id: int
    prob_id: int
    model_version: Literal["production", "development"] | int

    def get_registered_model_uri(self) -> str:
        true_model_version = self.model_version
        if self.model_version == "latest":
            ...
        model_name = f"phase{self.phase_id}-prob{self.prob_id}/"
        model_uri = Path("model:/", model_name, true_model_version)
        return str(model_uri)

    def get_model(
        self,
    ) -> PyFuncModel:
        """
        Get model from mlflow.
        """
        return load_model(self.get_registered_model_uri())

    def resolve_prediction(self, data: PyFuncOutput) -> List[Any]:
        """
        Turn `prediction` into `List[Any]`. `prediction` is generated from `self.model.predict()`
        """
        return data.to_list()
