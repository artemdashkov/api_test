import requests

# POST запрос с JSON телом
# url_pet_post = 'https://petstore.swagger.io/v2/pet'
# body_pet_post = {
#   "id": 0,
#   "category": {
#     "id": 0,
#     "name": "string"
#   },
#   "name": "doggie",
#   "photoUrls": [
#     "string"
#   ],
#   "tags": [
#     {
#       "id": 0,
#       "name": "string"
#     }
#   ],
#   "status": "available"
# }
# response = requests.post(
#     url=url_pet_post,
#     json=body_pet_post
# )
#
# assert response.status_code == 200
# print(response.cookies)

#POST запрос с Data телом
response = requests.post(
  url="https://petstore.swagger.io/v2/pet/1/uploadImage",
  files={
    "file": ("unnamed.jpg", open('../unnamed.jpg', 'rb'), 'image/jpeg')
  }
)

print(response.json())
