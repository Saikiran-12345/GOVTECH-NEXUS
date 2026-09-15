from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_domain_health_flow():
    res = client.post(
        "/api/v1/domain/health",
        json={
            "reference_code": "REF-HEALTH-001",
            "title": "Health Record Sample",
            "category": "PRIMARY",
            "amount": 1000.0,
            "remarks": "Test entry"
        }
    )
    assert res.status_code == 201
    assert res.json()["reference_code"] == "REF-HEALTH-001"
