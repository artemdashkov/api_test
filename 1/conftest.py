import pytest

@pytest.fixture(
    scope="session",
    params=[
        "Chrome"
    ],
    autouse=True
)
def driver(request):
    return request.param