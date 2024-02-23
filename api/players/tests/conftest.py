import pytest

from main import app
from fastapi.testclient import TestClient


@pytest.fixture
def mock_app():
    return TestClient(app)


def noop(*args, **kwargs):
    pass
