from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserUpdate
from app.core.security import hash_password, verify_password, create_access_token



def atualizar_usuario(user_id: int, form: UserUpdate, db: Session) -> User:
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    user.name = form.name
    user.email = form.email

    if form.password:
        user.hashed_password = hash_password(form.password)

    db.commit()
    db.refresh(user)
    return user