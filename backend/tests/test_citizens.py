from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_citizen_profile_flow():
    # Register user first
    reg_res = client.post(
        "/api/v1/auth/register",
        json={
            "email": "citizentest@govtech.gov.in",
            "username": "citizen_test",
            "password": "Password123!",
            "full_name": "Test Citizen"
        }
    )
    user_id = reg_res.json()["id"]

    profile_res = client.post(
        "/api/v1/citizens/profile",
        json={
            "user_id": user_id,
            "national_id": "NAT-99887766",
            "date_of_birth": "1990-05-15",
            "gender": "MALE",
            "permanent_address": "123 Govt Colony, New Delhi",
            "current_address": "123 Govt Colony, New Delhi",
            "occupation": "Engineer",
            "annual_income": 800000
        }
    )
    assert profile_res.status_code == 201
    assert profile_res.json()["national_id"] == "NAT-99887766"
