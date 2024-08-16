import pytest


@pytest.fixture()
def setup():
    print("Launching Browser")
    yield
    print("Closing Browser")


