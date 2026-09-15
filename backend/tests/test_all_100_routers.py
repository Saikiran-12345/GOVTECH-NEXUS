"""
GovTech Nexus Pytest Suite - OpenAPI REST Routers Test
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check_endpoint():
    res = client.get("/api/v1/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] in ["ok", "degraded"]

def test_ping_check_endpoint():
    res = client.get("/api/v1/health/ping")
    assert res.status_code == 200
    data = res.json()
    assert data["ping"] == "pong"

def test_root_endpoint():
    res = client.get("/")
    assert res.status_code == 200
    data = res.json()
    assert "name" in data
