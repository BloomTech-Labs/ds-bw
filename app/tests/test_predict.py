from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_input():
    """Return 200 Success when input is valid."""
    response = client.post(
        '/predict',
        json={
        'recommendations' : recommendations
    }
    )
    body = response.json()
    assert response.status_code == 200
    assert body['recommendations'] in [True, False]
    assert len(body['recommendations']) == 10


def test_invalid_input():
    """Return 422 Validation Error when x1 is negative."""
    response = client.post(
        '/predict',
        json={
            'recommendations' : recommendations
        }
    )
    body = response.json()
    assert response.status_code == 422
    assert '' in body['detail'][0]['loc']
