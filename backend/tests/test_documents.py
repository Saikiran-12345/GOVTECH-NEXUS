from fastapi.testclient import TestClient
from app.main import app
from tests.test_org import get_auth_token

client = TestClient(app)

def test_document_verification_flow():
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}

    org_res = client.post("/api/v1/organizations", json={"name": "Org D", "code": "ORGD", "jurisdiction": "State"}, headers=headers)
    dept_res = client.post("/api/v1/organizations/departments", json={"organization_id": org_res.json()["id"], "name": "Dept D", "code": "DEPTD"}, headers=headers)
    office_res = client.post("/api/v1/organizations/offices", json={"department_id": dept_res.json()["id"], "name": "Office D", "code": "OFFD", "city": "Delhi", "state": "Delhi", "pincode": "110001"}, headers=headers)
    user_res = client.post("/api/v1/auth/register", json={"email": "docuser@gov.in", "username": "docuser", "password": "Password1!", "full_name": "Doc User"})
    srv_res = client.post("/api/v1/services", json={"department_id": dept_res.json()["id"], "service_code": "SRV-DOC", "name": "Doc Service", "category": "LICENSE"})
    app_res = client.post("/api/v1/applications", json={"service_id": srv_res.json()["id"], "citizen_user_id": user_res.json()["id"], "office_id": office_res.json()["id"]})

    doc_res = client.post(
        "/api/v1/documents",
        json={
            "application_id": app_res.json()["id"],
            "document_type": "ID_PROOF",
            "original_filename": "passport.pdf",
            "stored_filename": "stored_passport_123.pdf",
            "file_path": "/uploads/stored_passport_123.pdf",
            "file_size_bytes": 204800,
            "checksum_md5": "e10adc3949ba59abbe56e057f20f883e"
        }
    )
    assert doc_res.status_code == 201

    v_res = client.post(
        f"/api/v1/documents/{doc_res.json()['id']}/verify",
        json={"status": "VERIFIED", "notes": "Legible passport document"}
    )
    assert v_res.status_code == 200
    assert v_res.json()["verification_status"] == "VERIFIED"
