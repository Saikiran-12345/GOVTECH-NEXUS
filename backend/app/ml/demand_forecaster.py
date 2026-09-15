"""
GovTech Nexus Local ML Engine - Service Demand & Peak Volume Forecaster
Scikit-learn Ridge regression & time-series feature engineering pipeline
"""
import os
import pickle
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

MODEL_PATH = os.path.join(os.path.dirname(__file__), "demand_forecaster_model.pkl")

class DemandForecasterPipeline:
    def __init__(self):
        self.model = Ridge(alpha=1.0)
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

    def train_on_synthetic_data(self, samples=300):
        # Features: [day_of_week, month_of_year, holiday_indicator, active_citizens_count, marketing_campaign_active]
        X = np.random.rand(samples, 5)
        X[:, 0] = np.random.randint(0, 7, size=samples)  # 0 to 6
        X[:, 1] = np.random.randint(1, 13, size=samples) # 1 to 12
        X[:, 2] = np.random.choice([0, 1], size=samples, p=[0.9, 0.1])
        X[:, 3] = 1000 + X[:, 3] * 50000
        X[:, 4] = np.random.choice([0, 1], size=samples, p=[0.8, 0.2])

        # Target y: Expected daily application volume
        y = 50 + 10 * np.sin(X[:, 0]) + 5 * X[:, 1] - 30 * X[:, 2] + 0.005 * X[:, 3] + 100 * X[:, 4] + np.random.normal(0, 10, samples)
        y = np.clip(y, 10, 5000)

        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({"model": self.model, "scaler": self.scaler}, f)

    def predict_daily_demand(self, day_of_week: int, month: int, is_holiday: bool, active_citizens: int, campaign: bool) -> float:
        feat = np.array([[day_of_week, month, 1 if is_holiday else 0, active_citizens, 1 if campaign else 0]])
        feat_scaled = self.scaler.transform(feat)
        pred = float(self.model.predict(feat_scaled)[0])
        return round(max(5.0, pred), 2)

demand_pipeline = DemandForecasterPipeline()
