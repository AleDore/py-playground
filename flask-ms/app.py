import os
from flask import Flask, jsonify, request, Response
from controllers.UserController import UserController

from utils.database import db

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

userController = UserController(db.session)


@app.route("/ping")
def ping():
    return jsonify({"ping": "pong"})


@app.route("/user", methods=["POST"])
def createUser():
    userJson = request.get_json(True)
    code, user = userController.createUser(userJson)
    return jsonify(user), code


@app.route("/users/<userId>")
def getUser(userId):
    code, user = userController.getUser(userId)
    return jsonify(user), code


@app.route("/users")
def getUsers():
    code, users = userController.getUsers()
    return jsonify(users), code


if __name__ == "__main__":
    app.run(debug=True)
