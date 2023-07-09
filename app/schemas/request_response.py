from pydantic import BaseModel
from typing import List, Any, Literal


class BaseSchema(BaseModel):
    id: str

    def __getitem__(self, item):
        return getattr(self, item)


class RequestSchema(BaseSchema):
    """Data Scheme of the Request Body,
    that will be received by `/predict` route

    - `id` of the request
    - `rows` contains names of features
    - `columns` 2D array data
    """

    columns: List[str]
    rows: List[List[None| float| int| str| bool]]


class ResponseSchema(BaseSchema):
    """Data Scheme of the Response Body, that will be sent from /predict/ route

    - `id` of the corresponding request
    - `prediction` Arrays of predictions
    - `drift` determine if the data is drift
    """

    prediction: List[List[Any] | int | float]
    drift: Literal[1,0]


class MockResponseSchema(BaseSchema):
    """Data Scheme of the Test Response Body, that will be sent from test/.../predict/ route

    - `message` for debugging
    - `response_body` is the `ResponseSchema`
    """

    message: str
    response_body: ResponseSchema
