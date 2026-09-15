from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "GovTech Nexus"
    assert "version" in data

def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "services" in data
    assert data["services"]["api"] == "healthy"

def test_ping_endpoint():
    response = client.get("/api/v1/health/ping")
    assert response.status_code == 200
    assert response.json()["ping"] == "pong"
