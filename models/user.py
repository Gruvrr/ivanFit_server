from sqlalchemy import Integer, BigInteger, String, Boolean, Date, ForeignKey, Column, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    telegram_user_id = Column(BigInteger, unique=True, index=True)
    gender = Column(String(10))
    first_name = Column(String(255))
    last_name = Column(String(255))
    birth_date = Column(Date)
    phone_number = Column(String(50))
    email = Column(String(255))
    city = Column(String(255))
    subscription_days = Column(Integer)
    subscription_purchases = Column(Integer)
    is_subscription_active = Column(Boolean, default=False)

    meal_plans = relationship("UserMealPlan", backref="user")
    payments = relationship("Payments", backref="user")
    trainings = relationship("UserTraining", backref="user")


class UserMealPlan(Base):
    __tablename__ = 'user_meal_plan'

    id = Column(Integer, primary_key=True)
    telegram_user_id = Column(BigInteger, ForeignKey('users.telegram_user_id'))
    week_number = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    nutrition_plan_meal_id = Column(Integer, ForeignKey('nutrition_plan_meal.id'))


class Payments(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    telegram_user_id = Column(BigInteger, ForeignKey('users.telegram_user_id'))
    unique_payload = Column(String(255), nullable=False)
    amount = Column(Integer, nullable=False)
    currency = Column(String(10))
    status = Column(String(50), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    error_message = Column(Text)


class UserTraining(Base):
    __tablename__ = 'user_trainings'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    training_number = Column(Integer)
    is_sent = Column(Boolean)
    sent_date = Column(DateTime)
    training_id = Column(Integer)

