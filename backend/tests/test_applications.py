from fastapi.testclient import TestClient
from app.main import app
from tests.test_org import get_auth_token

client = TestClient(app)

def test_application_flow():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    org_res = client.post("/api/v1/organizations", json={"name": "Org A", "code": "ORGA", "jurisdiction": "State"}, headers=headers)
    dept_res = client.post("/api/v1/organizations/departments", json={"organization_id": org_res.json()["id"], "name": "Dept A", "code": "DEPTA"}, headers=headers)
    office_res = client.post("/api/v1/organizations/offices", json={"department_id": dept_res.json()["id"], "name": "Office A", "code": "OFFA", "city": "Delhi", "state": "Delhi", "pincode": "110001"}, headers=headers)
    user_res = client.post("/api/v1/auth/register", json={"email": "appuser@gov.in", "username": "appuser", "password": "Password1!", "full_name": "App User"})
    srv_res = client.post("/api/v1/services", json={"department_id": dept_res.json()["id"], "service_code": "SRV-TEST", "name": "Test Service", "category": "LICENSE"})

    app_res = client.post(
        "/api/v1/applications",
        json={
            "service_id": srv_res.json()["id"],
            "citizen_user_id": user_res.json()["id"],
            "office_id": office_res.json()["id"],
            "form_data": {"applicant_name": "App User", "purpose": "Testing"}
        }
    )
    assert app_res.status_code == 201
    assert "APP-" in app_res.json()["application_number"]
