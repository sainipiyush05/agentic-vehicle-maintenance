from fastapi import Header, HTTPException
from supabase.client import Client
from backend.api.config.env import SUPABASE_URL, SUPABASE_KEY

supabase: Client = Client(SUPABASE_URL, SUPABASE_KEY)

def get_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing token")

    token = authorization.replace("Bearer ", "")
    user = supabase.auth.get_user(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return user
