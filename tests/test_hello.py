from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_hello_world():
    response = client.get("/api/v1/hello/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_hello_name():
    response = client.get("/api/v1/hello/name/Fausto")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Fausto!"}
