from api.users import Users
from api.user import User


# this is where your api endpoints should be registered
def register(api):
    api.add_resource(Users, "/api/v1/users")
    api.add_resource(User, "/api/v1/users/<int:id>")
