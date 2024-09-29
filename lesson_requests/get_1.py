import requests

url = 'https://petstore.swagger.io/v2/pet/'
pet_id = 1

response = requests.get(
    url=url+str(pet_id),
    headers={
        "accept":'application/json'
    }
)

print(response.json())