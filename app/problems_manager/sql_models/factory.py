from ..base_factory import BaseFactory
from .base import BaseSQLModel

class SQLModelsFactory(BaseFactory):
    
    def get_model(self) -> BaseSQLModel:
        pass
