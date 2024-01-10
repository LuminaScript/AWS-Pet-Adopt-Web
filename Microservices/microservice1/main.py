from fastapi import FastAPI, HTTPException, Depends
from db_connections import engine, SessionLocal, Base
from model.PetOwner import PetOwner
from pydantic import BaseModel
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class PetOwnerCreate(BaseModel):
    Name: str
    Email: str
    Telephone: str
    State: str
    City: str


class PetOwnerResponse(BaseModel):
    PetOwnerID: str
    Name: str
    Email: str
    Telephone: str
    State: str
    City: str
    Pets: dict


@app.get('/')
def home():
    return {'message': 'Pet Owner Service is running.'}


@app.post('/createpetowner', response_model=PetOwnerResponse)
def create_pet_owner(pet_owner: PetOwnerCreate, db: Session = Depends(get_db)):
    new_owner = PetOwner(Name=pet_owner.Name, Email=pet_owner.Email, Telephone=pet_owner.Telephone, State=pet_owner.State, City=pet_owner.City, Pets={})
    db.add(new_owner)
    db.commit()
    db.refresh(new_owner)
    return new_owner


@app.get('/getowner/{id}', response_model=PetOwnerResponse)
def get_pet_owner(id: str, db: Session = Depends(get_db)):
    owner = db.query(PetOwner).filter(PetOwner.PetOwnerID == id).first()
    if owner:
        return owner
    else:
        raise HTTPException(status_code=404, detail="Owner not found")


@app.put('/updatepetowner/{id}', response_model=PetOwnerResponse)
def update_pet_owner(id: str, pet_owner: PetOwnerCreate, db: Session = Depends(get_db)):
    owner_to_update = db.query(PetOwner).filter(PetOwner.PetOwnerID == id).first()
    if owner_to_update:
        owner_to_update.Name = pet_owner.Name
        owner_to_update.Email = pet_owner.Email
        owner_to_update.Telephone = pet_owner.Telephone
        owner_to_update.State = pet_owner.State
        owner_to_update.City = pet_owner.City
        db.commit()
        return owner_to_update
    else:
        raise HTTPException(status_code=404, detail="Owner not found")


@app.delete('/deletepetowner/{id}')
def delete_pet_owner(id: str, db: Session = Depends(get_db)):
    owner_to_delete = db.query(PetOwner).filter(PetOwner.PetOwnerID == id).first()
    if owner_to_delete:
        db.delete(owner_to_delete)
        db.commit()
        return {'message': f'Pet Owner {id} deleted successfully'}
    else:
        raise HTTPException(status_code=404, detail="Owner not found")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8012)
