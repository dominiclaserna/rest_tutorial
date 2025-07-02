from flask import Flask

from setups import setup_application

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello, world!"


# setup our server
setup_application(app)


if __name__ == "__main__":
    app.run("localhost", "8888", debug=True)
