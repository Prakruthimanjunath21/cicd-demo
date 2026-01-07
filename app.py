from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "branching" in response.json()["message"].lower()

