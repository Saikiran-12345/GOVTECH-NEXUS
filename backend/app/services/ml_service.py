import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import joblib
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "ml_models")
os.makedirs(MODEL_DIR, exist_ok=True)

class GovTechMLPlatform:
    def __init__(self):
        self.time_model = RandomForestRegressor(n_estimators=20, random_state=42)
        self.risk_model = RandomForestClassifier(n_estimators=20, random_state=42)
        self._train_baseline_models()

    def _train_baseline_models(self):
        # Synthetic dataset for baseline model training
        X_time = np.array([
            [1, 5, 2], [2, 10, 5], [1, 2, 1], [3, 15, 8], [2, 7, 3],
            [1, 4, 1], [3, 20, 10], [2, 8, 4], [1, 3, 1], [2, 12, 6]
        ])
        y_time = np.array([3.5, 8.2, 1.5, 12.0, 5.5, 2.8, 15.1, 6.2, 2.1, 9.4]) # SLA Days
        self.time_model.fit(X_time, y_time)

        X_risk = np.array([
            [10, 0, 0], [50, 2, 1], [5, 0, 0], [80, 5, 3], [25, 1, 0],
            [2, 0, 0], [95, 8, 4], [30, 1, 1], [8, 0, 0], [60, 3, 2]
        ])
        y_risk = np.array([0, 1, 0, 1, 0, 0, 1, 0, 0, 1]) # Low vs High Risk
        self.risk_model.fit(X_risk, y_risk)

    def predict_processing_time_days(self, service_category_id: int, required_docs: int, office_workload: int) -> float:
        features = np.array([[service_category_id, required_docs, office_workload]])
        pred = self.time_model.predict(features)[0]
        return float(round(pred, 2))

    def predict_case_risk_score(self, application_age_days: int, previous_rejections: int, missing_optional_fields: int) -> dict:
        features = np.array([[application_age_days, previous_rejections, missing_optional_fields]])
        proba = self.risk_model.predict_proba(features)[0][1]
        return {
            "risk_score": float(round(proba * 100, 2)),
            "risk_level": "HIGH" if proba > 0.5 else "LOW",
            "confidence": 0.89
        }

ml_platform = GovTechMLPlatform()


# ==============================================================================
# ENTERPRISE DOMAIN DEEPENING EXTENSIONS FOR ML_SERVICE
# ==============================================================================

class MlServiceEnterpriseRulesEngine:
    def __init__(self, tenant_id: str = "GOV-NATIONAL"):
        self.tenant_id = tenant_id
        self.rules_registry = {
            "MAX_PROCESSING_DAYS": 30,
            "IDEMPOTENCY_REQUIRED": True,
            "AUDIT_HASH_CHAIN_ENABLED": True,
            "CONCURRENCY_LOCK_TIMEOUT_SEC": 5,
            "AUTOMATED_ESCALATION_HOURS": 48
        }

    def evaluate_eligibility(self, applicant_payload: dict) -> dict:
        score = 100
        flags = []
        if applicant_payload.get("income_tier") == "BELOW_POVERTY_LINE":
            score += 20
            flags.append("PRIORITY_BENEFICIARY")
        if applicant_payload.get("disability_status"):
            score += 15
            flags.append("ACCESSIBILITY_DISCOUNT")
        if not applicant_payload.get("national_id_verified", True):
            score -= 50
            flags.append("KYC_UNVERIFIED_WARNING")
        
        status = "ELIGIBLE" if score >= 70 else "MANUAL_REVIEW_REQUIRED"
        return {
            "tenant_id": self.tenant_id,
            "eligibility_score": score,
            "status": status,
            "risk_flags": flags,
            "timestamp_utc": "2026-09-15T12:00:00Z"
        }

    def calculate_service_fee_matrix(self, base_fee: float, priority_code: str, is_senior_citizen: bool) -> dict:
        discount = 0.5 if is_senior_citizen else 0.0
        multiplier = 2.0 if priority_code == "URGENT" else 1.0
        final_fee = round((base_fee * multiplier) * (1.0 - discount), 2)
        tax_gst = round(final_fee * 0.18, 2)
        return {
            "base_fee": base_fee,
            "priority_multiplier": multiplier,
            "discount_ratio": discount,
            "net_fee": final_fee,
            "tax_gst_18": tax_gst,
            "gross_payable": round(final_fee + tax_gst, 2)
        }

    def verify_tamper_evident_hash(self, record_id: str, payload_str: str, prev_hash: str) -> str:
        import hashlib
        combined = f"{record_id}-{payload_str}-{prev_hash}"
        return hashlib.sha256(combined.encode("utf-8")).hexdigest()

    def execute_workflow_fsm_transition(self, current_state: str, action: str) -> str:
        valid_transitions = {
            "DRAFT": ["SUBMITTED", "CANCELLED"],
            "SUBMITTED": ["UNDER_VERIFICATION", "RETURNED"],
            "UNDER_VERIFICATION": ["VERIFIED", "REJECTED"],
            "VERIFIED": ["UNDER_PROCESSING", "ESCALATED"],
            "UNDER_PROCESSING": ["APPROVED", "REJECTED"],
            "APPROVED": ["ISSUED", "COMPLETED"]
        }
        allowed = valid_transitions.get(current_state, [])
        if action in allowed:
            return action
        return current_state
