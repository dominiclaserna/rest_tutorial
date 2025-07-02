import pytest
from myapp import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_successful_update_user(client):
    response = client.put(
        "/api/v1/users/1",
        data={
            "firstname": "updated",
            "lastname": "user",
        },
    )
    assert response.status_code == 200
    assert response.json["msg"] == "user updated successfully"

    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "firstname": "updated",
        "lastname": "user",
    }


def test_failed_update_user_not_found(client):
    response = client.put(
        "/api/v1/users/999",
        data={
            "firstname": "missing",
            "lastname": "user",
        },
    )
    assert response.status_code == 404
    assert response.json["error"] == "user not found"

def test_successful_delete_user(client):
    # Create a user
    response = client.post(
        "/api/v1/users",
        data={
            "firstname": "delete",
            "lastname": "me",
        },
    )
    assert response.status_code == 201
    assert response.json["msg"] == "successfully inserted new user"

    # just to get the last user's id
    response = client.get("/api/v1/users")
    users_list = response.json
    new_user = users_list[-1] 
    user_id = new_user["id"]


    response = client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    assert response.json["msg"] == "user deleted successfully"


    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 404
    assert response.json["error"] == "user not found"



def test_failed_delete_user_not_found(client):
    response = client.delete("/api/v1/users/999")
    assert response.status_code == 404
    assert response.json["error"] == "user not found"
