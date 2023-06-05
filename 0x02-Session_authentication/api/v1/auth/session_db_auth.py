#!/usr/bin/env python3
""" Module of auth
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """Sessions in database, inherits from other class"""
    def create_session(self, user_id=None):
        """creates and stores new instance of UserSession"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        k = {'user_id': user_id, 'session_id': session_id}
        u = UserSession(**k)
        u.save()
        u.save_to_file()
        return session_id
      
    def user_id_for_session_id(self, session_id=None):
        """returns the User ID by requesting UserSession in the db"""
        if session_id is None:
            return None
        u = UserSession.all()
        if not u:
            return None
        for i in u:
            if i.session_id == session_id:
                return i.user_id
        return None

    def destroy_session(self, request=None):
        """destroys the UserSession based on the Session ID"""
        if request is None:
            return None
        c = self.session_cookie(request)
        if c is None:
            return None
        u = UserSession.all()
        if not u:
            return None
        for i in u:
            if i.session_id == c:
                i.remove()
