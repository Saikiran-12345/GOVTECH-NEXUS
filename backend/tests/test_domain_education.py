from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_domain_education_flow():
    res = client.post(
        "/api/v1/domain/education",
        json={
            "reference_code": "REF-EDUCATION-001",
            "title": "Education Record Sample",
            "category": "PRIMARY",
            "amount": 1000.0,
            "remarks": "Test entry"
        }
    )
    assert res.status_code == 201
    assert res.json()["reference_code"] == "REF-EDUCATION-001"
