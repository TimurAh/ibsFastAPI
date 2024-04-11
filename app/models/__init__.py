from datetime import datetime
from typing import Union, List

from pydantic import BaseModel, Field


class ConverterRequest(BaseModel):
    number: Union[int, str]


class ConverterResponse(BaseModel):
    arabic: int
    roman: str


class User(BaseModel):
    name: str
    age: int = Field(gt=0,lt=100)
    adult: bool #= True if age >= 18 else False на потом или как вопрос, как сделать красиво)
    message: str | None

class MappingModel(BaseModel):
    list_of_ids:List[int | str]
    tags: str = "Стажировка"

class Meta(BaseModel):
    last_modification: datetime
    list_of_skills: List[str] | None
    mapping: MappingModel

class BigJson(BaseModel):
    """Использует модель User."""
    user: User
    meta: Meta



# class UserRequest(BaseModel):
#     name: str
#     message: str
#
#
# class User(BaseModel):
#     name: str
#     age: str
#     is_adult: bool
#     message: str = None
#
#
# class UserResponse(BaseModel):
#     pass
