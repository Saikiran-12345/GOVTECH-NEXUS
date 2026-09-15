"""
GovTech Nexus Local ML Engine - Application Fraud & Risk Scorer
Scikit-learn GradientBoostingClassifier pipeline
"""
import os
import pickle
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler

MODEL_PATH = os.path.join(os.path.dirname(__file__), "risk_scorer_model.pkl")

class RiskScorerPipeline:
    def __init__(self):
        self.model = GradientBoostingClassifier(n_estimators=40, random_state=42)
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
        # Features: [income_tier_code, document_checksum_verified, resubmission_count, address_mismatch, kyc_score]
        X = np.random.rand(samples, 5)
        X[:, 0] = np.random.randint(1, 4, size=samples)  # 1=LOW, 2=MID, 3=HIGH
        X[:, 1] = np.random.choice([0, 1], size=samples, p=[0.1, 0.9])
        X[:, 2] = np.random.randint(0, 5, size=samples)
        X[:, 3] = np.random.choice([0, 1], size=samples, p=[0.8, 0.2])
        X[:, 4] = 0.5 + X[:, 4] * 0.5

        # Target: Risk classification (0=LOW, 1=HIGH)
        risk_score = 0.3 * (3 - X[:, 0]) + 0.4 * (1 - X[:, 1]) + 0.2 * X[:, 2] + 0.5 * X[:, 3] - 0.3 * X[:, 4]
        y = (risk_score > 0.4).astype(int)

        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({"model": self.model, "scaler": self.scaler}, f)

    def evaluate_risk(self, income_code: int, doc_verified: bool, resubmissions: int, address_mismatch: bool, kyc_score: float) -> dict:
        feat = np.array([[income_code, 1 if doc_verified else 0, resubmissions, 1 if address_mismatch else 0, kyc_score]])
        feat_scaled = self.scaler.transform(feat)
        prob = float(self.model.predict_proba(feat_scaled)[0][1])
        risk_level = "HIGH" if prob > 0.5 else "MEDIUM" if prob > 0.25 else "LOW"
        return {"risk_probability": round(prob, 4), "risk_level": risk_level}

risk_pipeline = RiskScorerPipeline()
