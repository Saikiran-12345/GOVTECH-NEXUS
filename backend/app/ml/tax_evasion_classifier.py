"""
GovTech Nexus ML Engine - Commercial Tax GST Evasion Risk Classifier
Scikit-learn GradientBoostingClassifier pipeline
"""
import os, pickle, numpy as np
from sklearn.ensemble import GradientBoostingClassifier

MODEL_PATH = os.path.join(os.path.dirname(__file__), "tax_evasion_classifier_model.pkl")

class TaxEvasionClassifierPipeline:
    def __init__(self):
        self.model = GradientBoostingClassifier(n_estimators=30, random_state=42)
        self.is_trained = False
        self._bootstrap()

    def _bootstrap(self):
        if os.path.exists(MODEL_PATH):
            try:
                with open(MODEL_PATH, "rb") as f:
                    self.model = pickle.load(f)["model"]
                    self.is_trained = True
                return
            except Exception:
                pass
        self.train()

    def train(self, samples=200):
        # Features: [annual_turnover, reported_itc_claimed, invoice_discrepancy_count, audit_flags_history]
        X = np.random.rand(samples, 4)
        X[:, 0] *= 10000000 # turnover up to 10M
        X[:, 1] *= 1000000  # ITC up to 1M
        X[:, 2] = np.random.randint(0, 10, size=samples)
        X[:, 3] = np.random.randint(0, 5, size=samples)
        y = ((X[:, 2] * 0.3 + X[:, 3] * 0.4) > 0.8).astype(int)
        self.model.fit(X, y)
        self.is_trained = True
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({"model": self.model}, f)

    def classify_evasion_risk(self, turnover: float, itc_claimed: float, discrepancies: int, audit_flags: int) -> dict:
        feat = np.array([[turnover, itc_claimed, discrepancies, audit_flags]])
        prob = float(self.model.predict_proba(feat)[0][1])
        tier = "HIGH" if prob > 0.5 else "LOW"
        return {"evasion_risk_probability": round(prob, 4), "risk_tier": tier}

tax_evasion_pipeline = TaxEvasionClassifierPipeline()
