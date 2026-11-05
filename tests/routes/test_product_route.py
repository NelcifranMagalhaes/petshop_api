from tests.config_test import client

def test_product_creation_success(client):
    payload = {
        "name": "Sample Product",
        "price": 19.99,
        "description": "A sample product for testing.",
        "stock_quantity": 100
    }

    response = client.post("/products", json=payload)

    assert response.status_code == 201

    assert response.json()["name"] == payload["name"]
    assert float(response.json()["price"]) == float(payload["price"])
    assert response.json()["description"] == payload["description"]
    assert response.json()["stock_quantity"] == payload["stock_quantity"]

def test_product_creation_failure(client):
    payload = {
        "name": "", 
        "price": 19.99,
        "description": "A sample product for testing.",
        "stock_quantity": 100
    }

    response = client.post("/products", json=payload)

    assert response.status_code == 422