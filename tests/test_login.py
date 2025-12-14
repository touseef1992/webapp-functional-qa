# tests/test_login.py

def test_login_success(client):
    resp = client.post("/login", data={"email": "user1@example.com", "password": "correctpass"}, follow_redirects=True)
    assert resp.status_code == 200
    assert b"dashboard" in resp.data.lower() or b"logout" in resp.data.lower()

def test_login_failure_blank_password(client):
    resp = client.post("/login", data={"email": "user1@example.com", "password": ""}, follow_redirects=True)
    assert resp.status_code == 200

    # Should show short flash message "Enter password"
    assert b"enter password" in resp.data.lower()

    # Must not be logged in
    assert b"logout" not in resp.data.lower()
