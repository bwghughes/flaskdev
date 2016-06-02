import pytest
from hello import app
from flask import url_for

@pytest.fixture
def client():
    return app
    
def test_api_ping(client):
    res = client.get(url_for('hello_world'))
    assert "Hello" in res.content