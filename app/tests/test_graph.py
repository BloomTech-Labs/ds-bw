from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_input():
    """Return 200 Success for valid graph features."""
    response = client.get('/graph/graph')
    assert response.status_code == 200
    assert 'Illinois Unemployment Rate' in response.text


def test_invalid_input():
    """Return 404 if the endpoint isn't correct graph."""
    response = client.get('/graph/bad_response')
    body = response.json()
    assert response.status_code == 404
    assert body['detail'] == 'graph not found'