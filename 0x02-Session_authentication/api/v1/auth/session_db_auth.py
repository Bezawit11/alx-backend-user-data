#!/usr/bin/env python3
""" Module of auth
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User


class SessionDBAuth(SessionExpAuth):
    """Sessions in database, inherits from other class"""
    def create_session(self, user_id=None):
        """creates and stores new instance of UserSession"""
        
    def user_id_for_session_id(self, session_id=None):
        """returns the User ID by requesting UserSession in the db"""
        
    def destroy_session(self, request=None):
        """destroys the UserSession based on the Session ID"""
        
