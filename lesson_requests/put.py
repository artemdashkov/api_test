import requests

response = requests.put(
    url="https://petstore.swagger.io/v2/pet",
    json={
          "id": 1,
          "category": {
            "id": 0,
            "name": "string"
          },
          "name": "Alex",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "available"
        }
)

print(response.json())