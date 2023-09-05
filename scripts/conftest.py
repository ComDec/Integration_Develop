import pytest


@pytest.fixture(autouse=True)
def dummy_input():
    return 42
