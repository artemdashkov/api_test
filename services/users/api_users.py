import requests
from config.headers import Headers
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads

class UsersAPI:

    def __init__(self):
        self.headers = Headers()
        self.endpoints = Endpoints()
        self.payloads = Payloads()

    def get_user_list(self):
        response = requests.get(
            url=self.endpoints.list_all_users,
            headers=self.headers.basic
        )
        assert response.status_code == 200