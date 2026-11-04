import pytest
from fastapi.testclient import TestClient

# Import your FastAPI instance from your app directory
from app.main import app 

@pytest.fixture(scope="session")
def client():
    """Create a single TestClient instance shared across the test session."""
    with TestClient(app) as c:
        yield c
import pytest
from fastapi.testclient import TestClient

# Import your FastAPI instance from your app directory
from app.main import app 

@pytest.fixture(scope="session")
def client():
    """Create a single TestClient instance shared across the test session."""
    with TestClient(app) as c:
        yield c
