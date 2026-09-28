
import allure
from common.request import post


@allure.feature("租户管理")
@allure.story("新增租户")
@allure.title("新增租户成功")
def test_add_tenant(token):

    tenant_data = {
        "name": "自动化测试租户",
        "idcard": "110101199001011234",
        "mobile": "13800138000"
    }

    with allure.step("调用新增租户接口"):
        response = post(
            "/tenant/add",
            token,
            json=tenant_data
        )

        print("HTTP状态码：", response.status_code)
        print("响应内容：", response.text)

    with allure.step("校验HTTP状态码"):
        assert response.status_code == 200

    data = response.json()

    with allure.step("校验业务状态"):
        assert data.get("code") == 200
        assert data.get("msg") == "success"

    with allure.step("校验返回数据存在"):
        assert data.get("data") is not None

    tenant = data["data"]

    with allure.step("校验返回字段"):
        assert "id" in tenant
        assert "userId" in tenant
        assert "name" in tenant
        assert "mobile" in tenant
        assert "idcard" in tenant

    with allure.step("校验返回字段类型"):
        assert isinstance(tenant["id"], int)
        assert isinstance(tenant["userId"], int)
        assert isinstance(tenant["name"], str)
        assert isinstance(tenant["mobile"], str)
        assert isinstance(tenant["idcard"], str)

    with allure.step("校验返回数据与请求数据一致"):
        assert tenant["name"] == tenant_data["name"]
        assert tenant["mobile"] == tenant_data["mobile"]
        assert tenant["idcard"] == tenant_data["idcard"]

    print("新增租户ID：", tenant["id"])
