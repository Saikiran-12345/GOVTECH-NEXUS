"""
GovTech Nexus ML Engine - Industrial Environmental Safety Index Predictor
Scikit-learn ExtraTreesRegressor pipeline
"""
import os, pickle, numpy as np
from sklearn.ensemble import ExtraTreesRegressor

MODEL_PATH = os.path.join(os.path.dirname(__file__), "environmental_safety_model.pkl")

class EnvironmentalSafetyPipeline:
    def __init__(self):
        self.model = ExtraTreesRegressor(n_estimators=30, random_state=42)
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
        # Features: [carbon_emission_ppm, wastewater_ph, chemical_waste_kg, safety_drill_count]
        X = np.random.rand(samples, 4)
        X[:, 0] *= 400
        X[:, 1] = 6.0 + X[:, 1] * 3.0
        X[:, 2] *= 1000
        X[:, 3] = np.random.randint(1, 12, size=samples)
        y = 100 - (X[:, 0] * 0.1 + abs(7.0 - X[:, 1]) * 10 + X[:, 2] * 0.02 - X[:, 3] * 3)
        y = np.clip(y, 10, 100)
        self.model.fit(X, y)
        self.is_trained = True
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({"model": self.model}, f)

    def calculate_safety_index(self, carbon_ppm: float, ph: float, chemical_kg: float, safety_drills: int) -> dict:
        feat = np.array([[carbon_ppm, ph, chemical_kg, safety_drills]])
        score = float(self.model.predict(feat)[0])
        status = "COMPLIANT" if score >= 70 else "NON_COMPLIANT"
        return {"safety_index": round(score, 2), "compliance_status": status}

environmental_safety_pipeline = EnvironmentalSafetyPipeline()
