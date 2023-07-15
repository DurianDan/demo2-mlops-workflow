from typing import Tuple, Type, Literal
from pydantic import BaseModel, model_validator
from ..schemas import RequestSchema
from .predictor import PredictorFactory
from .predictor.base import BasePredictor
from .sql_models import SQLModelsFactory
from .sql_models.base import BaseSQLModel


class ProblemsManager(BaseModel):
    request_body: RequestSchema
    prob_id: int
    phase_id: int
    predictor_factory: PredictorFactory
    sql_model_factory: SQLModelsFactory
    ml_model_version: Literal["production", "development"] | int = "production"

    @model_validator(mode="before")
    def parse_factories(cls, values):
        """
        Automatically create the `self.predictor_factory` and `self.sql_model_factory` when `request_body` is parsed\n
        - Call `self.get_product_types()` to get the corresponding `predictor class` and `sql_model class`\n
        - Call `self.get_products(...)` to get the corresponding `predictor instaces` and `sql_model instance`\n
        - Call `self.get_factories()` to get the corresponding `factories`
        """
        values["predictor_factory"] = PredictorFactory(
            values["request_body"], values["prob_id"], values["phase_id"]
        )
        values["sql_model_factory"] = SQLModelsFactory(
            values["request_body"], values["prob_id"], values["phase_id"]
        )
        return values

    def get_factories(self) -> Tuple[PredictorFactory, SQLModelsFactory]:
        return self.predictor_factory, self.sql_model_factory

    def get_product_types(
        self,
    ) -> Tuple[Type[BasePredictor], Type[BaseSQLModel]]:
        if not hasattr(self, "predictor_type"):
            self.predictor_type = self.predictor_factory.get_predictor_type()
        if not hasattr(self, "sql_model_type"):
            self.sql_model_type = self.sql_model_factory.get_model_type()
        return (self.predictor_type, self.sql_model_type)

    def get_products(self) -> Tuple[BasePredictor, BaseSQLModel]:
        return (
            self.predictor_factory.get_predictor(self.ml_model_version),
            self.sql_model_factory.get_model(),
        )
