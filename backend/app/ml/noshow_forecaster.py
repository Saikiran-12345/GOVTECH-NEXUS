"""
GovTech Nexus ML Engine - Appointment No-Show Classifier
"""
import os, pickle, numpy as np
from sklearn.ensemble import RandomForestClassifier

MODEL_PATH = os.path.join(os.path.dirname(__file__), "noshow_forecaster_model.pkl")

class NoShowForecasterPipeline:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=30, random_state=42)
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
        X[:, 0] = np.random.randint(0, 24, size=samples) # hour of day
        X[:, 1] = np.random.randint(0, 7, size=samples) # day of week
        X[:, 2] = np.random.randint(0, 5, size=samples) # past no-shows
        X[:, 3] = np.random.choice([0, 1], size=samples) # sms reminder sent
        y = ((X[:, 2] * 0.4 - X[:, 3] * 0.3) > 0.2).astype(int)
        self.model.fit(X, y)
        self.is_trained = True
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({"model": self.model}, f)

    def predict_noshow(self, hour: int, day_of_week: int, past_noshows: int, reminder_sent: bool) -> dict:
        feat = np.array([[hour, day_of_week, past_noshows, 1 if reminder_sent else 0]])
        prob = float(self.model.predict_proba(feat)[0][1])
        return {"noshow_probability": round(prob, 4), "risk": "HIGH" if prob > 0.5 else "LOW"}

noshow_pipeline = NoShowForecasterPipeline()
