from pydantic import BaseModel
from typing import List, Any, Literal
from pandas import DataFrame
from numpy import ndarray, array


class BaseSchema(BaseModel):
    id: str

    def __getitem__(self, item):
        return getattr(self, item)


class RequestSchema(BaseSchema):
    """Data Scheme of the Request Body,
    that will be received by `/predict` route
    - attributes:
        - `id` of the request
        - `rows` contains names of features
        - `columns` 2D array data
    - methods:
        - `get_frame()` returns a `pandas DataFrame`
        - `get_array()` returns a 2D `numpy array`
    """

    columns: List[str]
    rows: List[List[None | float | int | str | bool]]

    def get_frame(self) -> DataFrame:
        return DataFrame(data=self.rows, columns=self.columns)

    def get_array(self) -> ndarray:
        return array(self.rows)


class ResponseSchema(BaseSchema):
    """Data Scheme of the Response Body, that will be sent from /predict/ route

    - `id` of the corresponding request
    - `prediction` Arrays of predictions
    - `drift` determine if the data is drift
    """

    prediction: List[List[Any] | int | float]
    drift: Literal[1, 0]


class MockResponseSchema(BaseSchema):
    """Data Scheme of the Test Response Body, that will be sent from test/.../predict/ route

    - `message` for debugging
    - `response_body` is the `ResponseSchema`
    """

    message: str
    response_body: ResponseSchema
