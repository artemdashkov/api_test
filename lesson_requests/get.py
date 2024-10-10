import requests

# GET запрос без передачи параметров
response = requests.get(
    url='https://petstore.swagger.io/v2/store/inventory',
    headers={
        "api_key": "special-key"
    },

)
print('1.\t', response.text)
print('type response.text\t', type(response.text), '\n')

print('2.\t', response.json())
print('type response.json()\t', type(response.json()), '\n')

print('3.\t', response.status_code)
print('type response.status_code.\t', type(response.status_code), '\n')

print('4.\t', response.json()['status'])
print('type(response.json()["status"]) \t', type(response.json()['status']), '\n')


# GET запрос с указанием path-параметра: например "any-site.com/users/15df4s"

# GET запрос с указанием query-параметров
response = requests.get(
    url="https://petstore.swagger.io/v2/pet/findByStatus",
    headers={
        "api_key": "special-key"
    },
    params={
        "status": "available"
    }
)

print(response.json()[0]['tags'][0]['name'])