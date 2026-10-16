from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_analyst_endpoint_returns_safe_unconfigured_message():
    response = client.post("/cia/sql-analyst", json={"question": "Which products are low in stock?"})
    assert response.status_code == 503
    assert "not configured" in response.json()["detail"].lower()

def test_question_validation():
    response = client.post("/cia/sql-analyst", json={"question": "?"})
    assert response.status_code == 422
