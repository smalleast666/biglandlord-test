
import allure

from common.request import post
from common.db import query_one


@allure.feature("租户管理")
@allure.story("新增租户数据库校验")
@allure.title("新增租户后校验数据库")
def test_add_tenant_database(token):

    tenant_data = {
        "name": "数据库校验租户",
        "idcard": "110101199001019999",
        "mobile": "13800138099"
    }

    with allure.step("调用新增租户接口"):

        response = post(
            "/tenant/add",
            token,
            json=tenant_data
        )

    with allure.step("校验接口返回成功"):

        assert response.status_code == 200

        data = response.json()

        assert data.get("code") == 200
        assert data.get("msg") == "success"

    with allure.step("获取新增租户ID"):

        tenant = data["data"]

        tenant_id = tenant["id"]

        assert tenant_id is not None

    with allure.step("查询数据库中的租户"):

        sql = """
            SELECT id, user_id, name, mobile, idcard
            FROM bl_tenant
            WHERE id = %s
        """

        db_tenant = query_one(
            sql,
            (tenant_id,)
        )

    with allure.step("校验数据库记录存在"):

        assert db_tenant is not None

    with allure.step("校验数据库数据正确"):

        assert db_tenant["id"] == tenant_id
        assert db_tenant["name"] == tenant_data["name"]
        assert db_tenant["mobile"] == tenant_data["mobile"]
        assert db_tenant["idcard"] == tenant_data["idcard"]

