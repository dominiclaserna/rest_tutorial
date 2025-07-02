import pytest
from myapp import app


@pytest.fixture
def client():
    return app.test_client()


class TestUsers:

    def test_successful_fetching_users(self, client):
        response = client.get("/api/v1/users")

        assert response.status_code == 200
        assert response.json == [
            {
                "id": 1,
                "firstname": "foo",
                "lastname": "bar",
            }
        ]

    def test_successful_adding_user(self, client):
        response = client.post(
            "api/v1/users",
            data={
                "firstname": "not",
                "lastname": "christian",
            },
        )

        assert response.status_code == 201
        assert response.json["msg"] == "successfully inserted new user"

        # check if the new user reflected
        response = client.get("/api/v1/users")

        assert response.json[-1] == {
            "id": 2,
            "firstname": "not",
            "lastname": "christian",
        }

    def test_failed_adding_user(self, client):
        response = client.post(
            "api/v1/users",
            data={
                "firstname": "foo",
                "lastname": "bar",
            },
        )

        assert response.status_code == 400
        assert response.json["error"] == "user already exists!"
