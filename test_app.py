from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "CI/CD is working" in response.json()["message"]
    assert "I have known CI/CD"
