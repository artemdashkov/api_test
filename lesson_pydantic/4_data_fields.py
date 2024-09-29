# Наличие полей в Class и JSON
# Опциональные поля

from pydantic import BaseModel # Для того чтобы начать работать с дата классами
from typing import Optional


class UserModel(BaseModel):
    id: int
    name: str
    status: str
    # admin: bool ## например нет поля "admin"
    admin: Optional[bool] # или  admin: Optional[bool] = None - установка значения 'None' по умолчанию
response = {
    'id': 145,
    'name': 'Ivan',
    'status': 'active',
    'admin': True
}

user = UserModel(**response)
print(user)
print(user.admin)
