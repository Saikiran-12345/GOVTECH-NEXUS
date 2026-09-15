from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_auth_token():
    # Register & login user to get token
    reg_res = client.post(
        "/api/v1/auth/register",
        json={
            "email": "adminorg@govtech.gov.in",
            "username": "adminorg",
            "password": "Password123!",
            "full_name": "Admin Org"
        }
    )
    login_res = client.post(
        "/api/v1/auth/login",
        json={
            "username_or_email": "adminorg@govtech.gov.in",
            "password": "Password123!"
        }
    )
    return login_res.json()["access_token"]

def test_create_and_list_org():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    
    response = client.post(
        "/api/v1/organizations",
        json={
            "name": "Ministry of Urban Affairs",
            "code": "MUA",
            "jurisdiction": "National",
            "contact_email": "info@mua.gov.in"
        },
        headers=headers
    )
    assert response.status_code == 201
    data = response.json()
    assert data["code"] == "MUA"

    list_res = client.get("/api/v1/organizations")
    assert list_res.status_code == 200
    assert len(list_res.json()) >= 1
