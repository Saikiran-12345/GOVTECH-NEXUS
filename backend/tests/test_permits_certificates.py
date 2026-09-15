from fastapi.testclient import TestClient
from app.main import app
from tests.test_org import get_auth_token

client = TestClient(app)

def test_permits_and_certificates():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    org_res = client.post("/api/v1/organizations", json={"name": "Org PC", "code": "ORGPC", "jurisdiction": "State"}, headers=headers)
    dept_res = client.post("/api/v1/organizations/departments", json={"organization_id": org_res.json()["id"], "name": "Dept PC", "code": "DEPTPC"}, headers=headers)
    office_res = client.post("/api/v1/organizations/offices", json={"department_id": dept_res.json()["id"], "name": "Office PC", "code": "OFFPC", "city": "Delhi", "state": "Delhi", "pincode": "110001"}, headers=headers)
    user_res = client.post("/api/v1/auth/register", json={"email": "pcuser@gov.in", "username": "pcuser", "password": "Password1!", "full_name": "PC User"})
    srv_res = client.post("/api/v1/services", json={"department_id": dept_res.json()["id"], "service_code": "SRV-PC", "name": "PC Service", "category": "LICENSE"})
    app_res = client.post("/api/v1/applications", json={"service_id": srv_res.json()["id"], "citizen_user_id": user_res.json()["id"], "office_id": office_res.json()["id"]})

    permit_res = client.post("/api/v1/permits-certificates/permits", json={"application_id": app_res.json()["id"], "title": "Trade License Permit", "expiry_date": "2027-12-31T23:59:59"})
    assert permit_res.status_code == 201
    assert "PRM-" in permit_res.json()["permit_number"]

    cert_res = client.post("/api/v1/permits-certificates/certificates", json={"application_id": app_res.json()["id"], "title": "Official Trade Certificate"})
    assert cert_res.status_code == 201
    v_code = cert_res.json()["verification_code"]

    verify_res = client.get(f"/api/v1/permits-certificates/certificates/verify/{v_code}")
    assert verify_res.status_code == 200
    assert verify_res.json()["title"] == "Official Trade Certificate"
