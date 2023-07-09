from typing import Tuple, Optional
from pydantic import BaseModel, root_validator
from ..schemas import RequestSchema 
from .predictor import PredictorFactory
from .predictor.base import BasePredictor
from .sql_models import SQLModelsFactory
from .sql_models.base import BaseSQLModel


class ProblemsManager(BaseModel):
    request_body: RequestSchema
    predictor_factory: PredictorFactory
    sql_model_factory: SQLModelsFactory

    @root_validator
    def set_factories(cls, values):
        '''
        Auto create the `factories` when `request_body` is parsed
        '''
        values["predictor_factory"] = PredictorFactory(values['request_body'])
        values["sql_model_factory"] = SQLModelsFactory(values['request_body'])
        return values

    def get_factories(self) -> Tuple[PredictorFactory, SQLModelsFactory]:
        return self.predictor_factory,self.sql_model_factory
    
    def get_products(self) -> Tuple[BasePredictor,BaseSQLModel]:
        return (
            self.predictor_factory.get_predictor(),
            self.sql_model_factory.get_model())