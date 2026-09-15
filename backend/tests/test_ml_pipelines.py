"""
GovTech Nexus Pytest Suite - Complete 10 Local ML Pipelines Test Module
"""
import pytest
from app.ml.sla_predictor import sla_pipeline
from app.ml.risk_scorer import risk_pipeline
from app.ml.demand_forecaster import demand_pipeline
from app.ml.workload_detector import workload_pipeline
from app.ml.escalation_predictor import escalation_pipeline
from app.ml.noshow_forecaster import noshow_pipeline
from app.ml.procurement_anomaly import procurement_anomaly_pipeline
from app.ml.tariff_optimizer import tariff_optimizer_pipeline
from app.ml.environmental_safety import environmental_safety_pipeline
from app.ml.tax_evasion_classifier import tax_evasion_pipeline

def test_sla_predictor_inference():
    res = sla_pipeline.predict_processing_time(doc_count=3, age=35, workload=40, delay_days=2.0, priority=2)
    assert isinstance(res, float)
    assert res > 0.0

def test_risk_scorer_inference():
    res = risk_pipeline.evaluate_risk(income_code=2, doc_verified=True, resubmissions=1, address_mismatch=False, kyc_score=0.95)
    assert "risk_probability" in res
    assert "risk_level" in res
    assert res["risk_level"] in ["LOW", "MEDIUM", "HIGH"]

def test_demand_forecaster_inference():
    res = demand_pipeline.predict_daily_demand(day_of_week=1, month=5, is_holiday=False, active_citizens=25000, campaign=True)
    assert isinstance(res, float)
    assert res >= 5.0

def test_workload_detector_inference():
    res = workload_pipeline.detect_bottleneck(pending_cases=350, active_officers=4, avg_hours=95.0, escalation_rate=0.35)
    assert "is_bottleneck" in res
    assert "anomaly_score" in res
    assert "severity" in res

def test_escalation_predictor_inference():
    res = escalation_pipeline.predict_escalation(days_pending=12.5, priority=3, prev_escalations=2, dept_busy=True)
    assert "escalation_probability" in res
    assert "will_escalate" in res

def test_noshow_forecaster_inference():
    res = noshow_pipeline.predict_noshow(hour=10, day_of_week=2, past_noshows=1, reminder_sent=True)
    assert "noshow_probability" in res
    assert "risk" in res

def test_procurement_anomaly_inference():
    res = procurement_anomaly_pipeline.detect_bid_anomaly(bid_ratio=0.95, vendor_age_days=450, submission_speed_sec=5000.0, past_disqualifications=0)
    assert "is_suspicious_bid" in res
    assert "anomaly_score" in res

def test_tariff_optimizer_inference():
    res = tariff_optimizer_pipeline.optimize_tariff_rate(base_kwh=250.0, temp_c=32.0, is_commercial=True, peak_ratio=0.4)
    assert "estimated_optimal_rate" in res
    assert res["estimated_optimal_rate"] > 0.0

def test_environmental_safety_inference():
    res = environmental_safety_pipeline.calculate_safety_index(carbon_ppm=150.0, ph=7.2, chemical_kg=45.0, safety_drills=6)
    assert "safety_index" in res
    assert "compliance_status" in res

def test_tax_evasion_classifier_inference():
    res = tax_evasion_pipeline.classify_evasion_risk(turnover=5000000.0, itc_claimed=250000.0, discrepancies=1, audit_flags=0)
    assert "evasion_risk_probability" in res
    assert "risk_tier" in res
