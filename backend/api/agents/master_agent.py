from agents.prediction_agent import predict_failure
from agents.scheduling_agent import auto_schedule

def run_agent_pipeline(data):
    prediction = predict_failure(data)
    if prediction["risk"] > 0.7:
        auto_schedule(data["vehicle_id"])
    return prediction
