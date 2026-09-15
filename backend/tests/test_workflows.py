from fastapi.testclient import TestClient
from app.main import app
from tests.test_org import get_auth_token

client = TestClient(app)

def test_workflow_case_approval():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    org_res = client.post("/api/v1/organizations", json={"name": "Org W", "code": "ORGW", "jurisdiction": "State"}, headers=headers)
    dept_res = client.post("/api/v1/organizations/departments", json={"organization_id": org_res.json()["id"], "name": "Dept W", "code": "DEPTW"}, headers=headers)
    office_res = client.post("/api/v1/organizations/offices", json={"department_id": dept_res.json()["id"], "name": "Office W", "code": "OFFW", "city": "Delhi", "state": "Delhi", "pincode": "110001"}, headers=headers)
    user_res = client.post("/api/v1/auth/register", json={"email": "wfuser@gov.in", "username": "wfuser", "password": "Password1!", "full_name": "WF User"})
    srv_res = client.post("/api/v1/services", json={"department_id": dept_res.json()["id"], "service_code": "SRV-WF", "name": "WF Service", "category": "LICENSE"})
    app_res = client.post("/api/v1/applications", json={"service_id": srv_res.json()["id"], "citizen_user_id": user_res.json()["id"], "office_id": office_res.json()["id"]})

    case_res = client.post("/api/v1/workflows/cases", json={"application_id": app_res.json()["id"], "priority": "HIGH"})
    assert case_res.status_code == 201
    assert "CASE-" in case_res.json()["case_number"]

    appr_res = client.post(
        "/api/v1/workflows/approvals",
        json={
            "case_id": case_res.json()["id"],
            "approver_user_id": user_res.json()["id"],
            "action": "APPROVED",
            "comments": "All documentation verified."
        }
    )
    assert appr_res.status_code == 201
    assert appr_res.json()["action"] == "APPROVED"
