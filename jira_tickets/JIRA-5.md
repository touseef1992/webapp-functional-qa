# BUG-005 — Signup allows invalid email formats (Major)

**Summary:** Signup form accepts invalid email addresses like 'test.com'.

**Environment:** Local http://127.0.0.1:5000, Chrome

**Steps to Reproduce:**
1. Open /signup
2. Enter 'test.com' in email field and submit

**Actual Result:** Account created with invalid email.
**Expected Result:** Email validation should prevent invalid formats.
**Severity:** Major
**Priority:** P1
**Attachments:** evidence/screenshots/BUG-005.png

**Suggested Fix:** Implement RFC-compliant email validation on client/server-side.
