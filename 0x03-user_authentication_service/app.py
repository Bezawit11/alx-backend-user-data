#!/usr/bin/env python3
"""flask app for handling user authentication"""


from auth import Auth
from flask import Flask, jsonify, request, abort


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index() -> str:
    """homepage to our app; employs get request"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """Registers a new user if it doen't exist already"""
    try:
        email = request.form['email']
        pwd = request.form['password']
    except Exception:
        abort(401)
    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

@app.route('/sessions', methods=['POST'])
def login() -> str:
    """checks if session exists for the given user"""
    email = request.form['email']
    pwd = request.form['password']
    if AUTH.valid_login(email, pwd):
        session_id = AUTH.create_session(email)
        res = jsonify({"email": "<user email>", "message": "logged in"})
        res.set_cookie('session_id', session_id)
        return res
    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
