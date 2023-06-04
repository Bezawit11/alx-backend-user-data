#!/usr/bin/env python3
""" Module of auth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """basic authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """extract_base64_authorization_header"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        r = authorization_header.split(' ')[-1]
        return r

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """decodes base64"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            d = b64decode(base64_authorization_header.encode('utf-8'))
            return d.decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """extracts user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        else:
            a = decoded_base64_authorization_header.split(':', 1)
            return a[-2], a[-1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        try:
            all = User.search({'email': user_email})
        except Exception:
            return None
        for a in all:
            if a.is_valid_password(user_pwd):
                return a
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request"""
        hauth = self.authorization_header(request)
        if not hauth:
            return None
        enc = self.extract_base64_authorization_header(hauth)
        if not enc:
            return None
        dec = self.decode_base64_authorization_header(enc)
        if not dec:
            return None
        email, pwd = self.extract_user_credentials(dec)
        if not email or not pwd:
            return None
        user = self.user_object_from_credentials(email, pwd)
        return user
