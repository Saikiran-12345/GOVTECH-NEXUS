"""
GovTech Nexus ML Engine - Public Procurement Bid Anomaly Detector
Scikit-learn OneClassSVM anomaly detection pipeline
"""
import os, pickle, numpy as np
from sklearn.svm import OneClassSVM

MODEL_PATH = os.path.join(os.path.dirname(__file__), "procurement_anomaly_model.pkl")

class ProcurementAnomalyPipeline:
    def __init__(self):
        self.model = OneClassSVM(nu=0.1, kernel="rbf", gamma="scale")
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
        # Features: [bid_amount_ratio, vendor_registration_days, bid_submission_speed_seconds, past_disqualifications]
        X = np.random.rand(samples, 4)
        X[:, 0] = 0.8 + X[:, 0] * 0.4 # bid ratio close to estimated cost
        X[:, 1] *= 1000 # vendor age days
        X[:, 2] = 3600 + X[:, 2] * 86400 # submission speed
        X[:, 3] = np.random.choice([0, 1], size=samples, p=[0.9, 0.1])
        self.model.fit(X)
        self.is_trained = True
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({"model": self.model}, f)

    def detect_bid_anomaly(self, bid_ratio: float, vendor_age_days: int, submission_speed_sec: float, past_disqualifications: int) -> dict:
        feat = np.array([[bid_ratio, vendor_age_days, submission_speed_sec, past_disqualifications]])
        score = float(self.model.decision_function(feat)[0])
        is_anomaly = bool(self.model.predict(feat)[0] == -1)
        return {"is_suspicious_bid": is_anomaly, "anomaly_score": round(score, 4)}

procurement_anomaly_pipeline = ProcurementAnomalyPipeline()
