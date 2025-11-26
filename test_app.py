import pytest
from app import app

@pytest.fixture
def client():
    # Create a test client for the app
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test that the home page returns the correct text."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, Jenkins!" in response.data
