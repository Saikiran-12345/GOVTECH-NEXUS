from fastapi.testclient import TestClient
from app.main import app
from tests.test_org import get_auth_token

client = TestClient(app)

def test_appointments_and_queues():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    org_res = client.post("/api/v1/organizations", json={"name": "Org AQ", "code": "ORGAQ", "jurisdiction": "State"}, headers=headers)
    dept_res = client.post("/api/v1/organizations/departments", json={"organization_id": org_res.json()["id"], "name": "Dept AQ", "code": "DEPTAQ"}, headers=headers)
    office_res = client.post("/api/v1/organizations/offices", json={"department_id": dept_res.json()["id"], "name": "Office AQ", "code": "OFFAQ", "city": "Delhi", "state": "Delhi", "pincode": "110001"}, headers=headers)
    user_res = client.post("/api/v1/auth/register", json={"email": "aquser@gov.in", "username": "aquser", "password": "Password1!", "full_name": "AQ User"})
    srv_res = client.post("/api/v1/services", json={"department_id": dept_res.json()["id"], "service_code": "SRV-AQ", "name": "AQ Service", "category": "LICENSE"})

    apt_res = client.post(
        "/api/v1/queues-appointments/appointments",
        json={
            "citizen_user_id": user_res.json()["id"],
            "office_id": office_res.json()["id"],
            "service_id": srv_res.json()["id"],
            "scheduled_time": "2026-10-01T10:00:00"
        }
    )
    assert apt_res.status_code == 201

    ticket_res = client.post(
        "/api/v1/queues-appointments/tickets",
        json={
            "office_id": office_res.json()["id"],
            "citizen_user_id": user_res.json()["id"],
            "service_id": srv_res.json()["id"]
        }
    )
    assert ticket_res.status_code == 201
    assert "Q-" in ticket_res.json()["ticket_number"]
