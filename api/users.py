from flask_restx import Resource, reqparse

users = [
    {
        "id": 1,
        "firstname": "foo",
        "lastname": "bar",
    }
]


class Users(Resource):

    def get(self):
        return users

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("firstname", type=str, required=True)
        parser.add_argument("lastname", type=str, required=True)
        args = parser.parse_args()

        firstname = args["firstname"]
        lastname = args["lastname"]

        # avoid inserting duplicate user
        for user in users:
            if firstname != user["firstname"] or lastname != user["lastname"]:
                continue

            return {"error": "user already exists!"}, 400

        data_id = len(users) + 1

        users.append(
            {
                "id": data_id,
                "firstname": firstname,
                "lastname": lastname,
            }
        )

        return {"msg": "successfully inserted new user"}, 201
