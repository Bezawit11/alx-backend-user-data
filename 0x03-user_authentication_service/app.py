#!/usr/bin/env python3
"""API Routes for Authentication Service"""
from auth import Auth
from flask import Flask, jsonify, request, abort


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index() -> str:
    """homepage to our app; imploys get request"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """Registers a new user if it doen't exist already"""
    try:
        email = request.form['email']
        pwd = request.form['password']
    except Exception:
        abort(400)
    try:
        user = AUTH.register_user(email, pwd)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
