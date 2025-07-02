import endpoints

from flask_restx import Api


def setup_application(app):
    api = Api(app, doc="/swagger-ui")

    # register our restful api endpoints
    endpoints.register(api)
