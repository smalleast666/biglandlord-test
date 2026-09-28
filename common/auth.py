import requests

from config.config import BASE_URL


def login():
    response = requests.post(
        f"{BASE_URL}/user/login",
        json={
            "username": "admin",
            "password": "123456"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data.get("code") == 200

    token = data.get("data")

    assert token is not None
    assert token != ""

    return token