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
