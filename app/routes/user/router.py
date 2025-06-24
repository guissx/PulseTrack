from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import UserUpdate, UserRead
from app.services.user_service import atualizar_usuario
from app.core.security import get_current_user 

router = APIRouter()

@router.put("/{user_id}", response_model=UserRead)
def update_user(
    user_id: int, 
    form: UserUpdate, 
    db: Session = Depends(get_db), 
    user_data: dict = Depends(get_current_user)
):
    return atualizar_usuario(user_id, form, db)
