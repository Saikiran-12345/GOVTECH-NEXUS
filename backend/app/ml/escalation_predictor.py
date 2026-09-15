"""
GovTech Nexus ML Engine - Grievance SLA Escalation Predictor
"""
import os, pickle, numpy as np
from sklearn.linear_model import LogisticRegression

MODEL_PATH = os.path.join(os.path.dirname(__file__), "escalation_predictor_model.pkl")

class EscalationPredictorPipeline:
    def __init__(self):
        self.model = LogisticRegression(random_state=42)
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
        X = np.random.rand(samples, 4)
        X[:, 0] *= 30 # days pending
        X[:, 1] = np.random.randint(1, 4, size=samples) # priority
        X[:, 2] *= 10 # previous escalations
        X[:, 3] = np.random.choice([0, 1], size=samples) # department busy flag
        y = ((X[:, 0] * 0.1 + X[:, 2] * 0.3) > 1.5).astype(int)
        self.model.fit(X, y)
        self.is_trained = True
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({"model": self.model}, f)

    def predict_escalation(self, days_pending: float, priority: int, prev_escalations: int, dept_busy: bool) -> dict:
        feat = np.array([[days_pending, priority, prev_escalations, 1 if dept_busy else 0]])
        prob = float(self.model.predict_proba(feat)[0][1])
        return {"escalation_probability": round(prob, 4), "will_escalate": prob > 0.5}

escalation_pipeline = EscalationPredictorPipeline()
