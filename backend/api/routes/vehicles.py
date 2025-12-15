from backend.api.db.supabase_client import supabase
from fastapi import APIRouter

router = APIRouter()

@router.get("/vehicles")
def get_vehicles():
    return {"status": "ok"}
