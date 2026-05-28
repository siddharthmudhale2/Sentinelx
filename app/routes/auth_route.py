from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.utils.db_dependency import get_db
from app.core.security import hash_password

from app.schemas.user_schema import UserLogin
from app.core.security import verify_password
from app.core.security import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    # Check existing email
    existing_email = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    # Check existing username
    existing_username = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already taken"
        )

    # Hash password
    hashed_password = hash_password(user.password)

    # Create user object
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    # Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }
    

@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    # Find user by email
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    # Check user exists
    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Verify password
    password_valid = verify_password(
        user.password,
        existing_user.password
    )

    if not password_valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Generate JWT token
    access_token = create_access_token(
        data={
            "sub": existing_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }