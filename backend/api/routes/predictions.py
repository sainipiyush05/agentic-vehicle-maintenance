from fastapi import APIRouter
from backend.api.agents.prediction_agent import predict_failure_agent

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("/")
def predict(data: dict):
    return predict_failure_agent(data)
