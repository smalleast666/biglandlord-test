from common.request import post


def test_build_order(token, tenant_id):

    house_id = 1
    count = 1

    response = post(
        f"/order/build/{tenant_id}/{house_id}/{count}",
        token
    )

    print("租户ID：", tenant_id)
    print("HTTP状态码：", response.status_code)
    print("响应内容：", response.text)

    assert response.status_code == 200

    data = response.json()

    assert data.get("code") == 200
    assert data.get("msg") == "success"