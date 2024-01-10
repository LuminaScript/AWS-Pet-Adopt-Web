from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

from db_connection import base


class Pets(base):
    __tablename__ = "Pets"

    PetID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
    Owner = Column(String)
    OwnerID = Column(Integer)
    Category = Column(String)
    Age = Column(Integer)
    Color = Column(String)
    Breeds = Column(String)
    Gender = Column(String)
    Height = Column(Float)
    Length = Column(Float)
    Weight = Column(Float)
    Picture = Column(String)
    Conditions = Column(String)