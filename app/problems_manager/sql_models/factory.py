from ..base_factory import BaseFactory
from .base import BaseSQLModel
from typing import Type


class SQLModelsFactory(BaseFactory):
    # TODO: implementing this factory with `importlib`
    def get_model_type(self) -> Type[BaseSQLModel]:
        pass

    def get_model(self) -> BaseSQLModel:
        pass
