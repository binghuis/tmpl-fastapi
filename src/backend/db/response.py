from typing import Union
from pydantic import BaseModel


class StandardResponse(BaseModel):
    status: int
    data: Union[list, dict] = None
    message: Union[str, tuple] = None
    error: str
