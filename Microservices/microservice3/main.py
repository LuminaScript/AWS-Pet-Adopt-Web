from fastapi import FastAPI, requests, HTTPException
import requests
from pydantic import BaseModel, Field
import uvicorn
from starlette.responses import RedirectResponse

from db_connection import SessionLocal
from models.Pets import Pets
import logging
from sqlalchemy.exc import SQLAlchemyError
import boto3
import json
import os

from fastapi_pagination import Page, add_pagination, paginate
from fastapi_pagination.utils import disable_installed_extensions_check
disable_installed_extensions_check()

app = FastAPI()
add_pagination(app)

# AWS Cognito and Google OAuth Configuration
COGNITO_DOMAIN = 'cucc.auth.us-east-1.amazoncognito.com'
CLIENT_ID = '5qhaja3dc38rjh25r8brc0cu11'
REDIRECT_URI = 'http://localhost:8012/callback'

# AWS SNS Configuration
AWS_ACCESS_KEY_ID = 'AKIAYCUCWACYYMYVT5NA'
AWS_SECRET_ACCESS_KEY = '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'
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:555398594737:adoptor-contact'

sns_client = boto3.client('sns', 
                          aws_access_key_id=AWS_ACCESS_KEY_ID, 
                          aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                          region_name='us-east-1')


def publish_to_sns(message: str):
    try:
        sns_client.publish(TopicArn=SNS_TOPIC_ARN, Message=message)
    except Exception as e:
        print(f"Error publishing to SNS: {e}")

logger = logging.getLogger("uvicorn.error")

session = SessionLocal()

class PetOut(BaseModel):
    PetID: int
    Name: str
    Owner: str
    OwnerID: int
    Category: str
    Age: int
    Color: str
    Breeds: str
    Gender: str
    Height: float
    Length: float
    Weight: float
    Picture: str
    Conditions: str


@app.get("/")
def read_root():
    return {"message": "Hello, World! -- CD from branch main v2.0 during demo"}


@app.get("/Pets")
def get_all_pets():
    pets_query = session.query(Pets)
    return pets_query.all()

# With Pagination
# sample pagination request http://localhost:8011/Dogs?page=2&size=2
@app.get("/Dogs", response_model=Page[PetOut])
def get_all_dogs():
    pets_query = session.query(Pets).filter(Pets.Category == "dog")
    return paginate(pets_query.all())

@app.post("/create")
def create_pet( name: str, category: str, breed : str):
    try:
        pet = Pets(
            Name= name,
            Owner="the owner",
            OwnerID=568,
            Category=category,
            Age=2,
            Color="black",
            Breeds=breed,
            Gender="f",
            Height=3.8,
            Length=6,
            Weight=15,
            Picture="sample_url",
            Conditions="None"
        )
        session.add(pet)
        session.commit()
        publish_to_sns("Pet created")
        return {"Pet added": pet.PetID}
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error creating pet")

@app.put("/update_pet_name/{id}")
def update_to_white(
        id: int,
        name: str
):
    update_querry = session.query(Pets).filter(Pets.PetID == id)
    pet = update_querry.first()
    pet.Name = name
    session.add(pet)
    session.commit()
    return {"Message": "Pet name updated"}


@app.put("/update_to_white/{id}")
def update_to_white(
        id: int
):
    update_querry = session.query(Pets).filter(Pets.PetID == id)
    pet = update_querry.first()
    pet.Color = "white"
    session.add(pet)
    session.commit()
    # publish_to_sns(f"Updated pet {id} to white")
    return {"Message": "Pet color updated"}

@app.delete("/delete/{id}")
def delete_todo(id: int):
    pet = session.query(Pets).filter(Pets.PetID==id).first()
    session.delete(pet)
    session.commit()
    # publish_to_sns(f"Deleted pet {id}")
    return {"todo deleted": pet.PetID}

# Redirect to Cognito Hosted UI
@app.get("/login")
def login():
    login_url = f"https://{COGNITO_DOMAIN}/login?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=openid+email"
    return RedirectResponse(url=login_url)

# Callback endpoint to handle the response from Cognito
@app.get("/callback")
def callback(code: str):
    token_url = f"https://{COGNITO_DOMAIN}/oauth2/token"
    data = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(token_url, data=data, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid token response")
    tokens = response.json()
    return tokens


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
