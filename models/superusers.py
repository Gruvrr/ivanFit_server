from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Superuser(Base):
    __tablename__ = 'superusers'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    is_super = Column(Boolean, default=False)


class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)