from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

VALID_T = [2, 8, 3, 5, 1, 8, 13, 0, 6, 6, 10, 8, 0, 8, 0, 8]


def test_predict_valid_input():
    response = client.post("/v1/predict", json={"features": VALID_T})
    assert response.status_code == 200
    assert response.json()["predicted_class"] == "19"


def test_predict_wrong_length():
    response =  client.post("/v1/predict", json={"features": [1, 2, 3]})                       
    assert response.status_code == 422                             


def test_predict_out_of_range():
      bad = VALID_T.copy()
      bad[2] = 100
      response =  client.post("/v1/predict", json={"features": bad}) 
      assert response.status_code == 422                                     