"""
GovTech Nexus Pytest Suite - Local ML Pipelines Test Module
"""
import pytest
from app.ml.sla_predictor import sla_pipeline
from app.ml.risk_scorer import risk_pipeline
from app.ml.demand_forecaster import demand_pipeline
from app.ml.workload_detector import workload_pipeline
from app.ml.escalation_predictor import escalation_pipeline
from app.ml.noshow_forecaster import noshow_pipeline

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
    assert res["severity"] in ["NORMAL", "WARNING", "CRITICAL"]

def test_escalation_predictor_inference():
    res = escalation_pipeline.predict_escalation(days_pending=12.5, priority=3, prev_escalations=2, dept_busy=True)
    assert "escalation_probability" in res
    assert "will_escalate" in res
    assert isinstance(res["will_escalate"], bool)

def test_noshow_forecaster_inference():
    res = noshow_pipeline.predict_noshow(hour=10, day_of_week=2, past_noshows=1, reminder_sent=True)
    assert "noshow_probability" in res
    assert "risk" in res
    assert res["risk"] in ["LOW", "HIGH"]
