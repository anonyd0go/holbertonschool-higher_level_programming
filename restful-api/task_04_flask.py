#!/usr/bin/python3
from flask import Flask, jsonify, request
from markupsafe import escape


app = Flask(__name__)
users = {
    "jane": {
        "username": "jane", 
        "name": "Jane", 
        "age": 28, 
        "city": "Los Angeles"
        },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
        },
    }


@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "Ok"

@app.route("/user/<username>")
def user_page(username): # use escape() on username
    username = escape(username)
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"})

@app.route("/add_user", methods=['POST'])
def add_user():
    new_user = request.json
    username = new_user.get("username")
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username == users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()