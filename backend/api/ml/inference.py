from backend.api.ml.model import FailureModel
from backend.api.ml.feature_engineering import extract_features

model = FailureModel()

# Dummy pre-trained weights (hackathon-safe)
model.model.coef_ = [[0.03, 0.5, -0.2]]
model.model.intercept_ = [-5]
model.model.classes_ = [0, 1]

def predict_failure(data: dict):
    X = extract_features(data)
    risk = model.predict_proba(X)
    return {"failure_risk": round(risk, 2)}
