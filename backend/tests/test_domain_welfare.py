from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_domain_welfare_flow():
    res = client.post(
        "/api/v1/domain/welfare",
        json={
            "reference_code": "REF-WELFARE-001",
            "title": "Welfare Record Sample",
            "category": "PRIMARY",
            "amount": 1000.0,
            "remarks": "Test entry"
        }
    )
    assert res.status_code == 201
    assert res.json()["reference_code"] == "REF-WELFARE-001"
