from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models.user import User

router = APIRouter()


@router.get("/users/all")
def det_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = {
        "user_info": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone_number": user.phone_number,
            "meal_plans": user.meal_plans,
            "payments": user.payments,
            "trainings": user.trainings
        }
    }
    return user


@router.get("/users/{user_id}/details")
def get_user_details(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = {
        "user_info": user,
        "meal_plans": user.meal_plans,
        "payments": user.payments
    }
    return user_data


@router.put("/users/{user_id}/updateSubscriptionDays")
def update_subscription_days(user_id: int, subscription_days: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.subscription_days = subscription_days
    db.commit()

    return {"message": "Subscription days updated successfully"}


