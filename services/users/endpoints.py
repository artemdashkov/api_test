import os

STAGE = 'https://dev-gs.qa-playground.com/api/v1' if os.environ["STAGE"] == "dev" else "https://release-gs.qa-playground.com/api/v1"

class Endpoints:
    list_all_users = f"{STAGE}/users"