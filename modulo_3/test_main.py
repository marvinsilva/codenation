from unittest.mock import Mock

import pytest

from main import get_temperature, requests


@pytest.fixture
def forecast_temperature(monkeypatch):
    resp_mock = Mock()
    temperature = 62
    resp_mock.json.return_value = {
        'latitude': -14.235004,
        'longitude': -51.92528,
        'timezone': 'America/Cuiaba',
        'currently': {
            'temperature': temperature,
        }
    }

    def mock_get(*args, **kwargs):
        return resp_mock

    monkeypatch.setattr(requests, 'get', mock_get)
    return int((temperature - 32) * 5.0 / 9.0)


def test_get_temperature_by_lat_lng(forecast_temperature):
    """ Unit test"""
    temperature = get_temperature('-14.235004', '-51.92528')
    assert forecast_temperature == temperature


def test_get_temperature_by_lat_lng_integration():
    """ Integration test"""
    assert get_temperature('-14.235004', '-51.92528') is not None
