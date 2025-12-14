# tests/test_dashboard_and_session.py

def test_dashboard_access_requires_login(client):
    # when not logged in, dashboard redirects to login or shows login form
    resp = client.get("/dashboard", follow_redirects=True)
    assert resp.status_code == 200
    # Expect the login form (or login text) to be present for non-authenticated users
    assert b"<form" in resp.data or b"login" in resp.data.lower()

def test_session_persistence(client):
    # login, then access dashboard. Use follow_redirects=True so session cookie persists.
    login_resp = client.post("/login",
                             data={"username": "user1", "password": "correctpass"},
                             follow_redirects=True)
    # If login succeeded, dashboard or welcome should appear in the response
    assert login_resp.status_code == 200
    assert (b"dashboard" in login_resp.data.lower() or b"welcome" in login_resp.data.lower() or b"<form" not in login_resp.data)

    # Now explicitly request the dashboard (no redirects) -- should be accessible
    dash_resp = client.get("/dashboard")
    # If the app still redirects (returns 302), follow redirects and ensure dashboard shown
    if dash_resp.status_code == 302:
        dash_resp = client.get("/dashboard", follow_redirects=True)
    assert dash_resp.status_code == 200
    assert b"dashboard" in dash_resp.data.lower() or b"welcome" in dash_resp.data.lower()
