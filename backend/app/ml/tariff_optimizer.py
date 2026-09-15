"""
GovTech Nexus ML Engine - Water & Power Tariff Demand Optimizer
Scikit-learn MLPRegressor neural network pipeline
"""
import os, pickle, numpy as np
from sklearn.neural_network import MLPRegressor

MODEL_PATH = os.path.join(os.path.dirname(__file__), "tariff_optimizer_model.pkl")

class TariffOptimizerPipeline:
    def __init__(self):
        self.model = MLPRegressor(hidden_layer_sizes=(16, 8), max_iter=200, random_state=42)
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
        # Features: [base_consumption_kwh, ambient_temp_c, commercial_zone_flag, peak_hour_ratio]
        X = np.random.rand(samples, 4)
        X[:, 0] *= 500
        X[:, 1] = 15 + X[:, 1] * 25
        X[:, 2] = np.random.choice([0, 1], size=samples)
        X[:, 3] *= 1.0
        y = 0.12 * X[:, 0] + 0.5 * X[:, 1] + 20 * X[:, 2] + 15 * X[:, 3] + np.random.normal(0, 2, samples)
        self.model.fit(X, y)
        self.is_trained = True
        with open(MODEL_PATH, "wb") as f:
            pickle.dump({"model": self.model}, f)

    def optimize_tariff_rate(self, base_kwh: float, temp_c: float, is_commercial: bool, peak_ratio: float) -> dict:
        feat = np.array([[base_kwh, temp_c, 1 if is_commercial else 0, peak_ratio]])
        pred_cost = float(self.model.predict(feat)[0])
        return {"estimated_optimal_rate": round(max(0.05, pred_cost), 2)}

tariff_optimizer_pipeline = TariffOptimizerPipeline()
