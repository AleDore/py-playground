from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)


@app.route("/ping")
def ping():
    return jsonify({"ping": "pong"})


@app.route("/user", methods=["POST"])
def createUser():
    userJson = request.get_json(True)
    print(userJson)
    return Response(json.dumps(userJson), 200)


if __name__ == "__main__":
    app.run(debug=True)
