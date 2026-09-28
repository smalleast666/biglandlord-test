from common.request import post


def test_add_tenant_without_token():

    tenant_data = {
        "name": "未登录测试",
        "idcard": "110101199001011234",
        "mobile": "13800138000"
    }

    response = post(
        "/tenant/add",
        json=tenant_data
    )

    print("HTTP状态码：", response.status_code)
    print("响应内容：", response.text)

    assert response.status_code == 401