import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_rating():
    response = client.post("/api/ratings/", json={"rating": 4})
    assert response.status_code == 200
    assert response.json() == {"rating": 4}