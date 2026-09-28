import requests
from config.config import BASE_URL


def get(path, token=None, params=None):
    headers = {}

    if token:
        headers["X-Token"] = token

    return requests.get(
        f"{BASE_URL}{path}",
        headers=headers,
        params=params
    )


def post(path, token=None, json=None):
    headers = {}

    if token:
        headers["X-Token"] = token

    return requests.post(
        f"{BASE_URL}{path}",
        headers=headers,
        json=json
    )