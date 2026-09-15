from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_domain_environment_flow():
    res = client.post(
        "/api/v1/domain/environment",
        json={
            "reference_code": "REF-ENVIRONMENT-001",
            "title": "Environment Record Sample",
            "category": "PRIMARY",
            "amount": 1000.0,
            "remarks": "Test entry"
        }
    )
    assert res.status_code == 201
    assert res.json()["reference_code"] == "REF-ENVIRONMENT-001"
