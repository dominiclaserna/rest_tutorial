from flask_restx import Resource

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
        pass

    def delete(self, id):
        pass
