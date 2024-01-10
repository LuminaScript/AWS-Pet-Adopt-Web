from db_connections import Base
from sqlalchemy import Column, String, JSON
from uuid import uuid4


class PetOwner(Base):
    __tablename__ = 'petowners_db2'

    PetOwnerID = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    Name = Column(String(50))
    Email = Column(String(50))
    Telephone = Column(String(50))
    State = Column(String(50))
    City = Column(String(50))
    Pets = Column(JSON)
