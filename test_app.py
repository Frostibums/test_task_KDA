import pytest
from fastapi.testclient import TestClient
from app import app, get_exchange_rate


@pytest.fixture
def test_client():
    client = TestClient(app)
    return client


def test_convert_currency(test_client):
    response = test_client.get("/api/rates?from=USD&to=RUB&value=1.0")
    assert response.status_code == 200
    data = response.json()
    assert 'result' in data
    assert isinstance(data['result'], float)


def test_convert_currency_invalid_currency(test_client):
    response = test_client.get("/api/rates?from=ABC&to=RUB&value=1.0")
    assert response.status_code == 404
    data = response.json()
    assert 'detail' in data
    assert "Failed to fetch ABC exchange rates!" in data.get('detail')


def test_convert_currency_currency_not_found(test_client):
    response = test_client.get("/api/rates?from=USD&to=ABC&value=1.0")
    assert response.status_code == 404
    data = response.json()
    assert 'detail' in data
    assert "Currency ABC not found in USD rates list!" in data.get('detail')


def test_get_exchange_rate():
    exchange_rate = get_exchange_rate("USD", "EUR")
    assert isinstance(exchange_rate, float)
