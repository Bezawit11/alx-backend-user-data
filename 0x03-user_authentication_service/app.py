#!/usr/bin/env python3
"""Basic Flask App"""

from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index() -> str:
    """jsonifies"""
    return jsonify({"message": "Bienvenue"})
 
@app.route('/users', methods=['POST'])
def users() -> str:
    """registers a user if it doesnt already exist"""
    try:
        email = request.form['email']
        pwd = request.form['password']
    except Exception:
        abort(400)
    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
