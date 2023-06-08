#!/usr/bin/env python3
"""Basic Flask App"""

from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()

@app.route('/')
def index():
    """jsonifies"""
    return jsonify({"message": "Bienvenue"})
 
@app.route('/users', methods=['POST'])
def users():
    """registers a user"""
    email = request.headers.get('email')
    pwd = request.headers.get('password')
    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": "<registered email>", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
