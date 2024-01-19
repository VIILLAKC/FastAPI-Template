from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    response = client.get("/api/v1")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}