import pytest


@pytest.fixture
def max_requests() -> int:
    return 5


@pytest.fixture
def time_span() -> int:
    return 60
