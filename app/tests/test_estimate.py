from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_input():
    """Return 200 Success when input is valid."""
    response = client.post(
        '/estimate-salt',
        json={
            'username': 'seviuqyelsdnirb'
        }
    )
    body = response.json()
    assert response.status_code == 200
    assert -1 <= body['avg_sentiment_score'] <= 1


def test_invalid_input():
    """Return 422 Validation Error when there is no input key or value."""
    response = client.post(
        '/estimate-salt',
        json={
        }
    )
    body = response.json()
    assert response.status_code == 422
    assert 'username' in body['detail'][0]['loc']
