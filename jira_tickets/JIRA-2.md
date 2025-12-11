# BUG-008 — Passwords printed in browser console logs (Critical)

**Summary:** Sensitive information (password) is being logged to console during signup.

**Environment:** Local http://127.0.0.1:5000, Chrome

**Steps to Reproduce:**
1. Open devtools console
2. Perform signup with test credentials
3. Observe console for logs

**Actual Result:** Password value appears in console logs.
**Expected Result:** Sensitive values must not be logged.
**Severity:** Critical
**Priority:** P0
**Attachments:** evidence/screenshots/BUG-008.png

**Suggested Fix:** Remove logging of sensitive fields; use safe logging practices.
