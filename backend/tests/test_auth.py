from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_citizen_registration():
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "citizen@govtech.gov.in",
            "username": "citizen123",
            "password": "Password123!",
            "full_name": "Citizen User",
            "phone_number": "+919876543210"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "citizen@govtech.gov.in"
    assert data["username"] == "citizen123"
    assert "id" in data

def test_user_login_success():
    # Login with existing registered citizen
    response = client.post(
        "/api/v1/auth/login",
        json={
            "username_or_email": "citizen@govtech.gov.in",
            "password": "Password123!"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"
    assert data["user"]["email"] == "citizen@govtech.gov.in"

def test_login_invalid_password():
    response = client.post(
        "/api/v1/auth/login",
        json={
            "username_or_email": "citizen@govtech.gov.in",
            "password": "WrongPassword!"
        }
    )
    assert response.status_code == 401
    assert "Invalid credentials" in response.json()["detail"]

def test_get_current_user_profile():
    # Login to get token
    login_res = client.post(
        "/api/v1/auth/login",
        json={
            "username_or_email": "citizen@govtech.gov.in",
            "password": "Password123!"
        }
    )
    token = login_res.json()["access_token"]

    me_res = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert me_res.status_code == 200
    data = me_res.json()
    assert data["email"] == "citizen@govtech.gov.in"
