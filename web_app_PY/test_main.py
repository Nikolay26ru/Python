import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_read_task():
    response = client.post("/tasks/", json={"title": "Test", "description": "Desc"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test"
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert any(task["title"] == "Test" for task in response.json())
