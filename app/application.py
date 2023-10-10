import requests
import json
from app import app
from flask import jsonify, request


@app.route("/")
def index():
    return "Micro services with Docker and Flask <br> By: Biebras and YuelinXin <br> 2023-04-21"


@app.route("/foo")
def get_service_1():
    response = {"foo": "bar"}
    return jsonify(response)


@app.route("/get_service_2")
def get_service_2():
    response = requests.get("http://service-2:8002/service_2/api_1")
    return response.json()


@app.route("/post", methods=["POST"])
def post_service_1():
    data = request.json
    return data


@app.route("/post_service_2")
def post_service_2():
    data = {"key": "value"}
    response = requests.post("http://service-2:8002/service_2/api_2", json=data)
    return response.json()
