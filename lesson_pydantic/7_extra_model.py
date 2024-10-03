from pydantic import BaseModel, Extra

class DynamicModel(BaseModel):
    class Config:
        extra = 'allow'

class UserModel(DynamicModel):
    name: str
    age: int
    status: str
    # tarif: str = None

response = {
    "name": "Ivan",
    "age": 25,
    "status": "Helthy",
     "admin": True
}

model = UserModel(**response)
print(model.admin)