# BUG-001 — Signup accepts .exe file as profile upload (Major)

**Summary:** File upload does not validate file types and allows executable files.

**Environment:** Local http://127.0.0.1:5000, Chrome

**Steps to Reproduce:**
1. Login and navigate to profile
2. Upload a .exe file and save

**Actual Result:** .exe file uploaded and displayed as download link.
**Expected Result:** Only image file types should be allowed (png,jpg); other types rejected.
**Severity:** Major
**Priority:** P1
**Attachments:** evidence/screenshots/BUG-001.png

**Suggested Fix:** Validate file MIME types and file extensions on server-side.
