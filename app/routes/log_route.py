from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.models.security_log_model import SecurityLog

from app.schemas.security_log_schema import (
    SecurityLogCreate
)

from app.utils.db_dependency import get_db

from app.utils.current_user import (
    get_current_user
)

router = APIRouter(
    prefix="/logs",
    tags=["Security Logs"]
)


@router.post("/create")
def create_log(
    log: SecurityLogCreate,
    db: Session = Depends(get_db),
    #current_user=Depends(get_current_user)
):
    


    new_log = SecurityLog(
        event_type=log.event_type,
        ip_address=log.ip_address,
        username=log.username,
        severity=log.severity
    )

    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return {
        "message": "Security log created successfully",
        "log_id": new_log.id
    }
    
@router.get("/all")
def get_all_logs(
    db: Session = Depends(get_db)
):

    logs = db.query(
        SecurityLog
    ).order_by(
        SecurityLog.created_at.desc()
    ).all()

    return logs