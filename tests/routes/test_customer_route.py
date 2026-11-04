from tests.config_test import client

def test_customer_creation_sucess(client):
    payload = {
        "name": "John Doe",
        "phone": "123-456-7890",
        "pets": "Dog, Cat"
    }

    response = client.post("/customers", json=payload)

    assert response.status_code == 201

    assert response.json()["name"] == payload["name"]
    assert response.json()["phone"] == payload["phone"]
    assert response.json()["pets"] == payload["pets"]

def test_customer_creation_failure(client):
    payload = {
        "name": "", 
        "phone": "123-456-7890",
        "pets": "Dog, Cat"
    }

    response = client.post("/customers", json=payload)

    assert response.status_code == 422