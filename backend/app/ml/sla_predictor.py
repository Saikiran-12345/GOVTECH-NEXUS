"""
GovTech Nexus Local ML Engine - SLA Processing Time Predictor
Scikit-learn RandomForestRegressor pipeline with feature preprocessing
"""
import os
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

MODEL_PATH = os.path.join(os.path.dirname(__file__), "sla_predictor_model.pkl")

class SlaPredictorPipeline:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=50, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False
        self._bootstrap_if_missing()

    def _bootstrap_if_missing(self):
        if os.path.exists(MODEL_PATH):
            try:
                with open(MODEL_PATH, "rb") as f:
                    data = pickle.load(f)
                    self.model = data["model"]
                    self.scaler = data["scaler"]
                    self.is_trained = True
                return
            except Exception:
                pass
        self.train_on_synthetic_data()

    def train_on_synthetic_data(self, samples=200):
        # Features: [doc_count, applicant_age, department_workload, historical_delay_days, priority_level]
        X = np.random.rand(samples, 5)
        X[:, 0] *= 10  # doc_count: 0 to 10
        X[:, 1] = 18 + X[:, 1] * 65  # age: 18 to 83
        X[:, 2] *= 100  # workload: 0 to 100
        X[:, 3] *= 15  # delay: 0 to 15
        X[:, 4] = np.random.randint(1, 4, size=samples)  # priority: 1, 2, 3

        # Target: processing days
        y = 1.5 * X[:, 0] + 0.05 * X[:, 1] + 0.1 * X[:, 2] + 0.8 * X[:, 3] - 0.5 * X[:, 4] + np.random.normal(0, 1, samples)
        y = np.clip(y, 1.0, 30.0)

        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({"model": self.model, "scaler": self.scaler}, f)

    def predict_processing_time(self, doc_count: int, age: int, workload: int, delay_days: float, priority: int) -> float:
        feat = np.array([[doc_count, age, workload, delay_days, priority]])
        feat_scaled = self.scaler.transform(feat)
        pred = self.model.predict(feat_scaled)[0]
        return float(round(max(0.5, pred), 2))

sla_pipeline = SlaPredictorPipeline()
