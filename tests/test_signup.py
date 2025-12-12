import pytest
from demo_webapp import app as demo_app

@pytest.fixture
def client():
    demo_app.app.config['TESTING'] = True
    with demo_app.app.test_client() as c:
        yield c

def test_signup_blank_password_rejected(client):
    resp = client.post("/signup", data={"email": "blankpass@example.com", "password": ""}, follow_redirects=True)
    assert b"Password is required" in resp.data or b"Password must be at least" in resp.data

def test_signup_short_password_rejected(client):
    resp = client.post("/signup", data={"email": "shortpass@example.com", "password": "abc"}, follow_redirects=True)
    assert b"Password must be at least" in resp.data
