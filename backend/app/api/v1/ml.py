from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.ml_service import ml_platform

router = APIRouter(prefix="/ml", tags=["Local Machine Learning Platform"])

class TimePredictRequest(BaseModel):
    service_category_id: int
    required_docs: int
    office_workload: int

class RiskPredictRequest(BaseModel):
    application_age_days: int
    previous_rejections: int
    missing_optional_fields: int

@router.post("/predict-processing-time")
def predict_processing_time(req: TimePredictRequest):
    days = ml_platform.predict_processing_time_days(req.service_category_id, req.required_docs, req.office_workload)
    return {"predicted_processing_days": days, "unit": "days", "model": "RandomForestRegressor-v1"}

@router.post("/predict-risk-score")
def predict_risk_score(req: RiskPredictRequest):
    res = ml_platform.predict_case_risk_score(req.application_age_days, req.previous_rejections, req.missing_optional_fields)
    return {"risk_assessment": res, "model": "RandomForestClassifier-v1"}
