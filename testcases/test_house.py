import pytest
from common.request import get


@pytest.mark.parametrize("house_id", [1, 2, 3])
def test_get_house_orders(token, house_id):

    current = 1
    size = 10
    desc = True

    response = get(
        f"/order/listByHouseId/{house_id}/{current}/{size}/{desc}",
        token
    )

    print("房源ID：", house_id)
    print("HTTP状态码：", response.status_code)
    print("响应内容：", response.text)

    assert response.status_code == 200

    data = response.json()
    assert data.get("code") == 200