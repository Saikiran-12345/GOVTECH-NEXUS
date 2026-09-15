from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ml_predictions():
    time_res = client.post(
        "/api/v1/ml/predict-processing-time",
        json={"service_category_id": 1, "required_docs": 3, "office_workload": 5}
    )
    assert time_res.status_code == 200
    assert "predicted_processing_days" in time_res.json()

    risk_res = client.post(
        "/api/v1/ml/predict-risk-score",
        json={"application_age_days": 40, "previous_rejections": 2, "missing_optional_fields": 1}
    )
    assert risk_res.status_code == 200
    assert "risk_assessment" in risk_res.json()
