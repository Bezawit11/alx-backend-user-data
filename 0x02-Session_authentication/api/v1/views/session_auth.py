#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def ses_auth():
    """returns user"""
    email = request.form.get('email')
    if not email:
        return jsonify({ "error": "email missing" }), 400
    pwd = request.form.get('password')
    if not pwd:
        return jsonify({ "error": "password missing" }), 400
    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    for i in user:
        if i.
