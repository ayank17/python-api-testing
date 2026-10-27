from api_client import APIClient

BASE_URL = "https://jsonplaceholder.typicode.com"
api = APIClient(BASE_URL)


def test_get_user():
    response = api.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "name" in data
    assert "email" in data


def test_get_all_users():
    response = api.get("/users")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
