# Вложенная модель и dataclass
from pydantic import BaseModel # Для того чтобы начать работать с дата классами

class Post(BaseModel):
    id: int
    content: str

class DataModel(BaseModel):
    id: int
    status: str
    tags: list[str]
    posts: dict[str, Post]


response = {
    'id': 1234,
    'status': 'active',
    'tags': ['music', 'people', 'greeting'],
    'posts': {
        "post_1":   {
                    'id': 1,
                    'content': 'Hello my dear friends'
                    },
        "post_2":   {
                    'id': 2,
                    'content': "Thing it's bad"
                    }
                }
}

model = DataModel(**response)
print(model.posts["post_1"].content)