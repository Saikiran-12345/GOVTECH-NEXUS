from fastapi.testclient import TestClient
from app.main import app
from tests.test_org import get_auth_token

client = TestClient(app)

def test_finance_payments():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    org_res = client.post("/api/v1/organizations", json={"name": "Org F", "code": "ORGF", "jurisdiction": "State"}, headers=headers)
    dept_res = client.post("/api/v1/organizations/departments", json={"organization_id": org_res.json()["id"], "name": "Dept F", "code": "DEPTF"}, headers=headers)
    office_res = client.post("/api/v1/organizations/offices", json={"department_id": dept_res.json()["id"], "name": "Office F", "code": "OFFF", "city": "Delhi", "state": "Delhi", "pincode": "110001"}, headers=headers)
    user_res = client.post("/api/v1/auth/register", json={"email": "fuser@gov.in", "username": "fuser", "password": "Password1!", "full_name": "F User"})
    srv_res = client.post("/api/v1/services", json={"department_id": dept_res.json()["id"], "service_code": "SRV-F", "name": "F Service", "category": "LICENSE"})
    app_res = client.post("/api/v1/applications", json={"service_id": srv_res.json()["id"], "citizen_user_id": user_res.json()["id"], "office_id": office_res.json()["id"]})

    pay_res = client.post(
        "/api/v1/finance/payments",
        json={
            "application_id": app_res.json()["id"],
            "citizen_user_id": user_res.json()["id"],
            "amount": 150.0,
            "payment_method": "UPI"
        }
    )
    assert pay_res.status_code == 201
    assert "TXN-" in pay_res.json()["transaction_reference"]
