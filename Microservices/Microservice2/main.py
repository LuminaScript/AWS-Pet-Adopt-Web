from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn
from db_connection import SessionLocal
from models.Adopter import Adopter
from fastapi import HTTPException


app = FastAPI()
session = SessionLocal()
class AdopterIn(BaseModel):
    name: str
    age: int
    email: str
    phone: str
class AdopterOut(BaseModel):
    id:int
    name:str
    age:int
    email:str
    phone:str
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/adopters")
def get_all_adopters():
    adopter_query = session.query(Adopter)
    return adopter_query.all()
@app.get("/adopter/{adopter_id}", response_model=AdopterOut)
def get_adopter(adopter_id: int):
    try:
        adopter = session.query(Adopter).filter(Adopter.id == adopter_id).first()
        if adopter is None:
            raise HTTPException(status_code=404, detail="Adopter not found")
        return adopter
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/adopter/create")
def create_pet():
    adopter = Adopter(
        name = "jason",
        age = 11,
        email = "czh2162216@gmail.com",
        phone = "001-1101010"
    )
    session.add(adopter)
    session.commit()
    return {"Adopter added": adopter.id}

@app.put("/adopter/{adopter_id}/update")
def update_to_white(adopter_id: int):
    update_querry = session.query(Adopter).filter(Adopter.id == adopter_id)
    adopter = update_querry.first()
    adopter.name = "white"
    session.add(adopter)
    session.commit()

@app.delete("/adopter/{adopter_id}/delete")
def delete_todo(adopter_id: int):
    adopter = session.query(Adopter).filter(Adopter.id==adopter_id).first()
    session.delete(adopter)
    session.commit()
    return {"todo deleted": adopter.id}