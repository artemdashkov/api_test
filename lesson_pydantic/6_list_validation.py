# Валидация списков
from pydantic import BaseModel, constr
from typing import Optional, Annotated

# Ситуация 1
class ResponseListModel(BaseModel):
    name: str
    last_name: Annotated[str, constr(max_length=50)]
    admin: Optional[bool] = None

response_1 = [
    {
        "name": "Ivan",
        "last_name": "Ivanov"
    },
    {
        "name": "Petr",
        "last_name": "Petrov"
    }
]

model_1 = ([ResponseListModel(**item) for item in response_1])


# Ситуация 2
class MainModel(BaseModel):
    items: list[ResponseListModel]

response_2 = {
    'items': [
    {
        "name": "Ivan",
        "last_name": "Ivanov"
    },
    {
        "name": "Petr",
        "last_name": "Petrov"
    }
]}

model_2 = MainModel(**response_2)
print(model_2.items[0].last_name)
