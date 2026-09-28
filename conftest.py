import pytest
from common.auth import login
from common.request import post
from common.data import load_yaml


@pytest.fixture
def token():
    return login()


@pytest.fixture
def tenant_id(token):

    data = load_yaml("test_data/tenant.yaml")

    tenant_data = data["tenant"]

    response = post(
        "/tenant/add",
        token,
        json=tenant_data
    )

    assert response.status_code == 200

    result = response.json()

    assert result.get("code") == 200

    tenant_id = result["data"]["id"]

    print("创建的租户ID：", tenant_id)

    return tenant_id