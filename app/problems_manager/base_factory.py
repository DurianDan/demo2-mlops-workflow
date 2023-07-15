from pydantic import BaseModel
from ..schemas import RequestSchema


class BaseFactory(BaseModel):
    request_body: RequestSchema
    phase_id: int
    prob_id: int
