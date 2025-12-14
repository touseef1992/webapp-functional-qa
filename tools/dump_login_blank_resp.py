import pathlib, sys
from demo_webapp.app import app as flask_app

# Use Flask test client
c = flask_app.test_client()
resp = c.post("/login", data={"username":"user1", "password": ""}, follow_redirects=True)

out = pathlib.Path("evidence/screenshots/debug_login_blank_response.html")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(resp.data)
print("Wrote response HTML to", out.resolve())
print("Response status:", resp.status_code)
# Print a snippet of the HTML for quick terminal check
print("First 400 chars of response:")
print(resp.data[:400])
