from abc import ABC, abstractmethod
from pandas import DataFrame
from numpy import array
from typing import List, Any


class BasePredictor(ABC):
    def __init__(
        self,
        data: DataFrame | array,
        columns: List[str] | None
    ) -> None:
        self.data = data

        self.columns = columns
        if type(data) == DataFrame:
            if columns: raise ValueError("columns must be empty if `data` is a `DataFrame`")
            self.columns = list(columns)
        elif not self.columns:
            raise ValueError("`columns` argument must be specified, or you must parse a `DataFrame`")
    

    @abstractmethod
    def predict(self) -> List[Any]:
        pass