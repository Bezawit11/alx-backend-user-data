#!/usr/bin/env python3
""" Module of auth
"""
from api.v1.auth.session_auth import SessionAuth
from base64 import b64decode
from models.user import User
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Now we will add an expiration date to a Session ID"""
    def __init__(self):
        """initialization"""
        ses = getenv("SESSION_DURATION")
        try:
          ses = int(ses)
        except Exception:
          ses = 0
        self.session_duration = ses
        
    def create_session(self, user_id=None):
        """returns session based on user id"""
        s = super().create_session(user_id)
        if s is None:
            return None
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[s] = session_dictionary
        return s
      
    def user_id_for_session_id(self, session_id=None):
        """return user_id from the session dictionary"""
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        r = self.user_id_by_session_id[session_id]
        if self.session_duration <= o:
            return r.get('user_id')
        if r.get('created_at') is None:
            return None
        t = self.session_duration + timedelta(r.get('created_at'))
        if t < datetime.now():
            return None
        return r.get('user_id')
