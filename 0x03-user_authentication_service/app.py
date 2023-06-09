#!/usr/bin/env python3
"""flask app for handling user authentication"""


from auth import Auth
from flask import Flask, jsonify, request, abort, redirect


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
        res = jsonify({"email": email, "message": "logged in"})
        res.set_cookie('session_id', session_id)
        return res
    abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """logs out a logged in user"""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    abort(403)


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """finds user based on the cookie session id"""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


@app.route('/reset_password', methods=['POST'])
def reset_token() -> str:
    """"resets the password of a user if the right credentials r provided"""
    try:
        email = request.form['email']
    except KeyError:
        abort(403)
    try:
        rtoken = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": rtoken}),  200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password() -> str:
    """returns 403 if invalid token
        updates password if the right info
        is given
    """
    try:
        email = request.form['email']
        reset_token = request.form['reset_token']
        new_pwd = request.form['new_password']
    except KeyError:
        abort(403)
    try:
        AUTH.update_password(reset_token, new_pwd)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
