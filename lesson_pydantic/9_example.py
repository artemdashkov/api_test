import requests
from pydantic import BaseModel

# GET запрос без передачи параметров

class ItemModel(BaseModel):
    Water: int
    Kk: int
    sold: int
    pq: int
    mDUJCEbfDCV: int
    Nacw: int
    string: int
    pending: int
    efzCALPvIDa: int
    available: int
    false: int
    rYZdP: int
    quavO: int
    VzPDTdcAr: int
    status: int
    e: int
    AdrOZtD: int
    HNTKlxCjupXlPjnccJQq: int
    nLlAOidJYvIze: int

response = requests.get(
    url='https://petstore.swagger.io/v2/store/inventory',
    headers={
        "api_key": "special-key"
    },

)

print(response.json())
model = ItemModel(**response.json())

print(model.sold)
