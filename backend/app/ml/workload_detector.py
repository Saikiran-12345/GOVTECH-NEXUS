"""
GovTech Nexus Local ML Engine - Department Workload & Bottleneck Detector
Scikit-learn IsolationForest anomaly & congestion detection pipeline
"""
import os
import pickle
import numpy as np
from sklearn.ensemble import IsolationForest

MODEL_PATH = os.path.join(os.path.dirname(__file__), "workload_detector_model.pkl")

class WorkloadDetectorPipeline:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.is_trained = False
        self._bootstrap_if_missing()

    def _bootstrap_if_missing(self):
        if os.path.exists(MODEL_PATH):
            try:
                with open(MODEL_PATH, "rb") as f:
                    self.model = pickle.load(f)["model"]
                    self.is_trained = True
                return
            except Exception:
                pass
        self.train_on_synthetic_data()

    def train_on_synthetic_data(self, samples=200):
        # Features: [pending_cases_count, active_officers_count, avg_resolution_hours, escalation_rate]
        X = np.random.rand(samples, 4)
        X[:, 0] *= 500  # cases: 0 to 500
        X[:, 1] = 2 + X[:, 1] * 20  # officers: 2 to 22
        X[:, 2] *= 120  # avg hours: 0 to 120
        X[:, 3] *= 0.5  # escalation rate: 0 to 50%

        self.model.fit(X)
        self.is_trained = True
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({"model": self.model}, f)

    def detect_bottleneck(self, pending_cases: int, active_officers: int, avg_hours: float, escalation_rate: float) -> dict:
        feat = np.array([[pending_cases, active_officers, avg_hours, escalation_rate]])
        score = float(self.model.decision_function(feat)[0])
        is_bottleneck = bool(self.model.predict(feat)[0] == -1)
        severity = "CRITICAL" if score < -0.15 else "WARNING" if is_bottleneck else "NORMAL"
        return {"is_bottleneck": is_bottleneck, "anomaly_score": round(score, 4), "severity": severity}

workload_pipeline = WorkloadDetectorPipeline()
