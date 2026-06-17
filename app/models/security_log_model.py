from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class SecurityLog(Base):
    __tablename__ = "security_logs"

    id = Column(Integer, primary_key=True, index=True)

    event_type = Column(String(100), nullable=False)

    ip_address = Column(String(50), nullable=False)

    username = Column(String(100), nullable=False)

    severity = Column(String(20), nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )