from pydantic import BaseModel

class Vehicle(BaseModel):
    vin: str
    owner_id: str
