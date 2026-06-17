from pydantic import BaseModel


class SecurityLogCreate(BaseModel):
    event_type: str
    ip_address: str
    username: str
    severity: str


class SecurityLogResponse(BaseModel):
    id: int
    event_type: str
    ip_address: str
    username: str
    severity: str

    class Config:
        from_attributes = True