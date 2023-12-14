from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models.superusers import Admin, Superuser
from dependencies import get_db
import bcrypt
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


class AdminRegistrationRequest(BaseModel):
    username: str
    password: str


def get_current_superuser(db: Session = Depends(get_db)):
    # Предположим, что текущий пользователь - это 'ваше_имя'
    current_user = db.query(Superuser).filter(Superuser.username == "Anton").first()
    if current_user and current_user.is_super:
        return current_user
    else:
        raise HTTPException(status_code=401, detail="Нет доступа")


@router.post("/admin/register")
def register_admin(request: AdminRegistrationRequest, db: Session = Depends(get_db), current_user: Superuser = Depends(get_current_superuser)):
    logger.info("Trying to register admin...")
    if not current_user.is_super:
        raise HTTPException(status_code=403, detail="Недостаточно прав")
    # Хеширование пароля
    hashed_password = bcrypt.hashpw(request.password.encode('utf-8'), bcrypt.gensalt())

    # Создание нового админа
    new_admin = Admin(username=request.username, hashed_password=hashed_password.decode('utf-8'))
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return {"message": "Администратор успешно зарегистрирован", "admin_id": new_admin.id}



