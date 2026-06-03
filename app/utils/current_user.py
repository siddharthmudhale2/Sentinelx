from fastapi import Depends

from sqlalchemy.orm import Session

from app.models.user_model import User

from app.utils.db_dependency import get_db

from app.core.security import (
    oauth2_scheme,
    verify_access_token
)

def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db)

):

    email = verify_access_token(token)

    user = db.query(User).filter(
        User.email == email
    ).first()

    return user
