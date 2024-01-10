from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

from db_connection import base


class Adopter(base):
    __tablename__ = "adopters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    phone = Column(String)