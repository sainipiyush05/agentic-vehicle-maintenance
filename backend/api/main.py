from fastapi import FastAPI
from backend.api.routes import vehicles, predictions

app = FastAPI(title="Agentic Vehicle Maintenance API")

app.include_router(vehicles.router)
app.include_router(predictions.router)

@app.get("/health")
def health():
    return {"status": "ok"}
