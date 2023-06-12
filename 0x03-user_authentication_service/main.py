#!/usr/bin/env python3
"""
Test file
"""
import requests

def register_user(email: str, password: str) -> None:
    """tests the registers user function"""
    url = http://0.0.0.0:5000/users
    p = {'email': email, 'password': password}
    res = requests.post(url, p=p)
    assert res.status_code == 200
    assert res.json() = {"email": email, "message": "user created"}

def log_in_wrong_password(email: str, password: str) -> None:
    """test for wrong password input during login"""
    url = http://0.0.0.0:5000/login
    p = {'email': email, 'password': password}
    res = requests.post(url, p=p)
    



EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
