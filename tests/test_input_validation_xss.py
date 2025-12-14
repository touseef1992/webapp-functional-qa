def test_basic_xss_protection(client):
    malicious = "<script>alert('xss')</script>"
    resp = client.post("/signup", data={"username":"attacker","password":"x", "email":"a@b.com", "bio": malicious}, follow_redirects=True)
    assert b"<script>" not in resp.data  # app should escape or reject
