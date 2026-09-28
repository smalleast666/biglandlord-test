# BigLandlord 接口自动化测试

基于 Python + Requests + Pytest 搭建的大房东租赁管理系统接口自动化测试项目。

本项目围绕登录、租户、订单等核心业务接口，完成接口功能测试、参数化测试、Token 鉴权、测试数据管理、数据库校验及基础性能测试。

## 一、项目介绍

本项目以 BigLandlord 租赁管理系统后端接口为测试对象，使用 Python 编写接口自动化测试脚本。

主要完成：

* 接口功能测试
* 正常场景与异常场景测试
* Token 登录鉴权
* 参数化测试
* YAML 测试数据管理
* 接口公共请求封装
* 数据库结果校验
* Allure 测试报告
* JMeter 接口性能测试
* Git 版本管理

## 二、技术栈

| 技术       | 用途        |
| -------- | --------- |
| Python   | 自动化测试脚本开发 |
| Requests | HTTP 接口请求 |
| Pytest   | 测试用例组织与执行 |
| PyYAML   | 测试数据管理    |
| MySQL    | 数据库校验     |
| Allure   | 测试报告      |
| JMeter   | 接口性能测试    |
| Git      | 版本管理      |

## 三、项目结构

```text
biglandlord-test
│
├── common
│   ├── auth.py             # 登录及 Token 获取
│   ├── request.py          # HTTP 请求封装
│   ├── data.py             # YAML 数据读取
│   └── db.py               # MySQL 数据库操作
│
├── config
│   └── config.py           # 项目配置
│
├── test_data
│   └── tenant.yaml         # 测试数据
│
├── testcases
│   ├── test_login.py       # 登录接口测试
│   ├── test_house.py       # 订单查询接口测试
│   ├── test_order.py       # 订单创建测试
│   ├── test_tenant.py      # 租户新增测试
│   ├── test_tenant_db.py  # 数据库校验
│   └── test_tenant_negative.py # 异常场景测试
│
├── conftest.py             # Pytest Fixture
├── pytest.ini              # Pytest 配置
├── .gitignore
└── README.md
```

## 四、测试内容

### 1. 登录接口测试

测试用户正常登录及错误密码场景。

正常登录验证：

* HTTP 状态码
* 业务状态码
* Token 是否正常返回

错误登录验证：

* 错误密码
* 错误登录响应

### 2. Token 鉴权测试

登录接口获取 JWT Token 后，在后续业务接口请求中通过 `X-Token` 请求头进行身份认证。

测试未登录情况下访问需要认证的接口，验证系统返回 `401`。

### 3. 租户新增测试

验证租户新增接口：

* HTTP 状态码
* 业务状态码
* 返回数据
* 返回字段
* 字段类型
* 请求数据与返回数据一致性

### 4. 参数化测试

针对订单查询接口使用 Pytest 参数化，对不同房源 ID 进行测试。

示例：

```python
@pytest.mark.parametrize("house_id", [1, 2, 3])
```

减少重复代码，提高测试用例复用性。

### 5. 数据库校验

接口新增租户成功后，通过 MySQL 查询数据库，验证接口操作是否真正写入数据库。

实现：

```text
接口请求
   ↓
接口返回成功
   ↓
获取业务数据
   ↓
查询 MySQL
   ↓
校验数据库数据
```

### 6. 异常场景测试

目前包含未登录访问接口的异常场景：

```text
无 Token
   ↓
访问需要认证的接口
   ↓
HTTP 401
```

同时在测试过程中发现：

> 租户新增接口目前可以接受格式异常的手机号，例如 `123`，接口仍返回成功并写入数据库。

该问题可作为测试过程中发现的接口校验缺陷进行记录。

## 五、测试执行

### 运行全部测试

在项目根目录执行：

```bash
pytest
```

### 查看详细执行信息

```bash
pytest -s
```

### 执行指定测试文件

例如：

```bash
pytest -s testcases/test_login.py
```

### 执行数据库测试

```bash
pytest -s testcases/test_tenant_db.py
```

## 六、测试结果

当前自动化测试用例：

```text
9 passed
```

最近一次完整执行结果：

```text
================ 9 passed in 0.87s ================
```

## 七、Allure 测试报告

项目使用 `allure-pytest` 生成测试结果。

执行：

```bash
pytest --alluredir=allure-results
```

生成报告：

```bash
allure serve allure-results
```

可以查看测试用例执行情况、测试步骤及测试结果。

## 八、JMeter 性能测试

使用 Apache JMeter 对接口进行基础性能测试。

测试流程：

```text
登录接口
   ↓
提取 JWT Token
   ↓
业务接口
   ↓
携带 X-Token 请求
```

通过 JMeter 的 JSON JMESPath Extractor 提取登录接口返回的 Token，并通过：

```text
X-Token: ${token}
```

传递给后续业务接口。

测试过程中完成了多用户、多次循环请求，并观察接口响应时间、吞吐量及错误率。

一次测试结果：

```text
登录接口：
请求数：500
平均响应时间：84 ms
错误率：0%

业务接口：
请求数：500
平均响应时间：12 ms
错误率：0%
```

## 九、项目收获

通过本项目熟悉了接口自动化测试的基本流程：

```text
测试需求分析
      ↓
设计测试场景
      ↓
准备测试数据
      ↓
Requests 调用接口
      ↓
Pytest 组织测试用例
      ↓
Token 鉴权
      ↓
参数化测试
      ↓
数据库校验
      ↓
Allure 测试报告
      ↓
JMeter 性能测试
      ↓
Git 版本管理
```

同时通过实际测试发现并记录接口参数校验问题，加深了对接口测试、异常场景测试和缺陷定位流程的理解。
