from api_client import APIClient


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_create_post():
    client = APIClient(BASE_URL)

    payload = {
        "title": "QA Automation Testing",
        "body": "Testing POST API using Python and Pytest",
        "userId": 1
    }

    response = client.post("/posts", payload)

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["title"] == payload["title"]
    assert response_data["body"] == payload["body"]
    assert response_data["userId"] == payload["userId"]
    assert "id" in response_data
