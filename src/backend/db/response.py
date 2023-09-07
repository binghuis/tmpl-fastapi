from typing import Union
from pydantic import BaseModel


class CRUD(BaseModel):
    data: Union[list, dict] = None
    message: Union[str, tuple] = None
