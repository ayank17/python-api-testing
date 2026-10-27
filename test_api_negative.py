from api_client import APIClient


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_nonexistent_post():
    client = APIClient(BASE_URL)

    response = client.get("/posts/999999")

    assert response.status_code == 404


def test_get_invalid_endpoint():
    client = APIClient(BASE_URL)

    response = client.get("/invalid-endpoint")

    assert response.status_code == 404


def test_create_post_with_empty_payload():
    client = APIClient(BASE_URL)

    response = client.post("/posts", {})

    assert response.status_code == 201

    response_data = response.json()

    assert isinstance(response_data, dict)
