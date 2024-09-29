import requests

import requests

HEADERS = {
    "Authorization":"any_token"
}

class TestUsers:
    # setup
    def setup(self):
        requests.post(
            url="any_url",
            headers=HEADERS
        )

    # get
    def test_patch_user(self):
        user_list = requests.get(
            url="any_url",
            headers=HEADERS
        )

        user = user_list.json()['items'][0]['uuid']
        old_user_name = user_list.json()['items'][0]['name']
        patched_user = requests.patch(
            url=f'any_utl{user}',
            headers=HEADERS,
            json={
                "name":"QWERTY"
            }
        )

        assert old_user_name != patched_user.json()['name']
