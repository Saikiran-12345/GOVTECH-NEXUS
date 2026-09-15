from fastapi.testclient import TestClient
from app.main import app
from tests.test_org import get_auth_token

client = TestClient(app)

def test_service_catalog():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    org_res = client.post("/api/v1/organizations", json={"name": "Org S", "code": "ORGS", "jurisdiction": "State"}, headers=headers)
    dept_res = client.post("/api/v1/organizations/departments", json={"organization_id": org_res.json()["id"], "name": "Dept S", "code": "DEPTS"}, headers=headers)

    service_res = client.post(
        "/api/v1/services",
        json={
            "department_id": dept_res.json()["id"],
            "service_code": "SRV-BIRTH-01",
            "name": "Birth Certificate Issue",
            "category": "CERTIFICATE",
            "fee": 50.0,
            "sla_days": 3
        }
    )
    assert service_res.status_code == 201
    assert service_res.json()["service_code"] == "SRV-BIRTH-01"
