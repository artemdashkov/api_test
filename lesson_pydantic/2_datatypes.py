# Автоматическое преобразование типов
from pydantic import BaseModel # Для того чтобы начать работать с дата классами

class UserModel(BaseModel):
    id: int
    name: str
    status: str
    admin: bool

response = {
    'id': '145w',
    'name': 'Ivan',
    'status': 'active',
    'admin': True
}

user = UserModel(**response)
print(user)
print(user.admin)
