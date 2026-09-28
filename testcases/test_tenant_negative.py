from common.request import post


def test_add_tenant_invalid_mobile(token):

    tenant_data = {
        "name": "测试租户",
        "idcard": "110101199001011234",
        "mobile": "123"
    }

    response = post(
        "/tenant/add",
        token,
        json=tenant_data
    )

    print("测试数据：", tenant_data)
    print("HTTP状态码：", response.status_code)
    print("响应内容：", response.text)

    # 我们期望非法手机号不能新增成功
    assert response.status_code != 200