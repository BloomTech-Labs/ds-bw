from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_input():
    """Return 200 Success for valid song features."""
    response = client.get('/features/features')
    assert response.status_code == 200
    assert 'features' in response.text


def test_invalid_input():
    """Return 404 if the endpoint isn't correct."""
    response = client.get('/features/bad_response')
    body = response.json()
    assert response.status_code == 404
    assert body['detail'] == 'features not found'