import requests
from config.config import BASE_URL


def test_login_success():
    response = requests.post(
        f"{BASE_URL}/user/login",
        json={
            "username": "admin",
            "password": "123456"
        }
    )

    print("HTTP状态码：", response.status_code)
    print("响应内容：", response.text)

    assert response.status_code == 200

    data = response.json()

    assert data.get("code") == 200
    assert data.get("data") is not None
    assert data.get("data") != ""


def test_login_wrong_password():
    response = requests.post(
        f"{BASE_URL}/user/login",
        json={
            "username": "admin",
            "password": "111111"
        }
    )

    print("错误登录 HTTP状态码：", response.status_code)
    print("错误登录响应：", response.text)

    assert response.status_code == 500
    assert "用户名或密码错误" in response.text