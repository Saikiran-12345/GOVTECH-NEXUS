from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_domain_taxation_flow():
    res = client.post(
        "/api/v1/domain/taxation",
        json={
            "reference_code": "REF-TAXATION-001",
            "title": "Taxation Record Sample",
            "category": "PRIMARY",
            "amount": 1000.0,
            "remarks": "Test entry"
        }
    )
    assert res.status_code == 201
    assert res.json()["reference_code"] == "REF-TAXATION-001"
