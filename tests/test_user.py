import pytest

from myapp import app


@pytest.fixture
def client():
    return app.test_client()


class TestUser:

    def test_succesful_fetching_a_user(self, client):
        response = client.get("api/v1/users/1")

        assert response.status_code == 200
        assert response.json == {
            "id": 1,
            "firstname": "foo",
            "lastname": "bar",
        }

    def test_failed_fetching_a_user(self, client):
        response = client.get("api/v1/users/999")

        assert response.status_code == 404
        assert response.json["error"] == "user not found"
