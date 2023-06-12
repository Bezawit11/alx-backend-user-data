#!/usr/bin/env python3
"""
Test file
"""
import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

def register_user(email: str, password: str) -> None:
    """tests the registers user function"""
    url = 'http://0.0.0.0:5000/users'
    p = {'email': email, 'password': password}
    res = requests.post(url, p=p)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "user created"}

def log_in_wrong_password(email: str, password: str) -> None:
    """test for wrong password input during login"""
    url = 'http://0.0.0.0:5000/login'
    p = {'email': email, 'password': password}
    res = requests.post(url, p=p)
    assert res.status_code == 401
    
def log_in(email: str, password: str) -> str:
    """logging in with the right credentials"""
    url = 'http://0.0.0.0:5000/login'
    p = {'email': email, 'password': password}
    res = requests.post(url, p=p)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "logged in"}
    
def profile_unlogged() -> None:
    """successful logout testing"""
    url = 'http://0.0.0.0:5000/sessions'
    res = requests.delete(url)
    assert res.status_code == 403
    
def profile_logged(session_id: str) -> None:
    """test to check if user is logged"""
    url = 'http://0.0.0.0:5000/profile'
    p = {'session_id', session_id}
    res = requests.get(url, p=p)
    assert res.status_code == 200
    
def log_out(session_id: str) -> None:
    """testing logout operation"""
    url = 'http://0.0.0.0:5000/sessions'
    res = requests.delete(url)
    assert res.status_code == 301
    
def reset_password_token(email: str) -> str:
    """testing for reset token func"""
    url = 'http://0.0.0.0:5000/reset_password'
    p = {'email': email}
    res = requests.post(url, p=p)
    assert res.status_code == 200
    tok = res.json().get('reset_token')
    assert res.json() == {'email': EMAIL, 'reset_token': tok}

def update_password(email: str, reset_token: str, new_password: str) -> None:
    """testing the update password func"""
    url = 'http://0.0.0.0:5000/reset_password'
    p = {'email': email, 'reset_token': reset_token, 'new_password':new_password}
    res = requests.post(url, p=p)
    assert res.status_code == 200
    asser res.json() == {"email": EMAIL, "message": "Password updated"}
    

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
