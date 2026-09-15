from fastapi.testclient import TestClient
from app.main import app
from tests.test_org import get_auth_token

client = TestClient(app)

def test_employee_creation():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    org_res = client.post("/api/v1/organizations", json={"name": "Org 1", "code": "ORG1", "jurisdiction": "State"}, headers=headers)
    dept_res = client.post("/api/v1/organizations/departments", json={"organization_id": org_res.json()["id"], "name": "Dept 1", "code": "DEPT1"}, headers=headers)
    office_res = client.post("/api/v1/organizations/offices", json={"department_id": dept_res.json()["id"], "name": "Office 1", "code": "OFF1", "city": "Delhi", "state": "Delhi", "pincode": "110001"}, headers=headers)
    user_res = client.post("/api/v1/auth/register", json={"email": "emp1@gov.in", "username": "emp1", "password": "Password1!", "full_name": "Employee One"})

    emp_res = client.post(
        "/api/v1/employees",
        json={
            "user_id": user_res.json()["id"],
            "department_id": dept_res.json()["id"],
            "office_id": office_res.json()["id"],
            "employee_code": "EMP-001",
            "designation": "Case Officer",
            "joining_date": "2024-01-01"
        }
    )
    assert emp_res.status_code == 201
    assert emp_res.json()["employee_code"] == "EMP-001"
