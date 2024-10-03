import pytest


@pytest.fixture(scope="function", params=[1, 2, 3])
def my_first_fixture(request):
    param_value = request.param
    print(f"Setup with param value: {param_value}")
    print(request.node.name)
    print(request.node.name)
    print(request.node.name)
    yield param_value * 2
    print(request.node.name)


@pytest.fixture()
def log_2():
    print("set Up test case 1111111")
    yield
    print("Tear down test case 1111111")


@pytest.fixture()
def log():
    print("set Up test case")
    yield
    print("Tear down test case")
