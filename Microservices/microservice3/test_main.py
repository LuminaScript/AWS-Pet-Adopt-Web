from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app=app)

def test_client():
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK