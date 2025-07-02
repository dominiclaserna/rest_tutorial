from flask_restx import Resource,reqparse

from api.users import users

# Resoure for a single user
# It has shared data coming from Users


class User(Resource):

    def get(self, id):
        for user in users:
            if id == user["id"]:
                return user

        return {"error": "user not found"}, 404

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("firstname", type=str, required=True)
        parser.add_argument("lastname", type=str, required=True)
        args = parser.parse_args()

        for user in users:
            if user["id"] == id:
                user["firstname"] = args["firstname"]
                user["lastname"] = args["lastname"]
                return {"msg": "user updated successfully"}, 200

        return {"error": "user not found"}, 404

    def delete(self, id):
        global users
        for i, user in enumerate(users):
            if user["id"] == id:
                users.pop(i)
                return {"msg": "user deleted successfully"}, 200

        return {"error": "user not found"}, 404
    
    # added post because wala lang hehe
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("firstname", type=str, required=True)
        parser.add_argument("lastname", type=str, required=True)
        args = parser.parse_args()

        firstname = args["firstname"]
        lastname = args["lastname"]

        # duplicates
        for user in users:
            if firstname == user["firstname"] and lastname == user["lastname"]:
                return {"error": "user already exists!"}, 400

        data_id = len(users) + 1
        users.append({
            "id": data_id,
            "firstname": firstname,
            "lastname": lastname,
        })

        return {"msg": "successfully inserted new user"}, 201