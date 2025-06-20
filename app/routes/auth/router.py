from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead, UserLogin
from app.services.auth_service import criar_usuario, autenticar_usuario
from app.database.database import get_db

router = APIRouter()

@router.post("/signup", response_model=UserRead)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return criar_usuario(user, db)

@router.post("/login")
def login(form: UserLogin, db: Session = Depends(get_db)):
    return autenticar_usuario(form, db)
