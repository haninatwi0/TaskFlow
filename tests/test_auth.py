import pytest

def test_example():
    assert True


def test_password_hash():
    from werkzeug.security import generate_password_hash, check_password_hash

    password = "TaskFlow123!"

    hashed = generate_password_hash(password)

    assert hashed != password
    assert check_password_hash(hashed, password)
    
    
    
    
import re

def test_valid_email():

    email = "hanin@example.com"

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    assert re.match(pattern, email)
    
    
    
def test_strong_password():

    password = "TaskFlow123!"

    assert len(password) >= 8
    assert any(c.isupper() for c in password)
    assert any(c.islower() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)