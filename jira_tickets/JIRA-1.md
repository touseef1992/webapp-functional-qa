# BUG-006 — Application vulnerable to XSS in input fields (Critical)

**Summary:** Input fields accept script tags which execute in the browser.

**Environment:** Local http://127.0.0.1:5000, Chrome latest

**Steps to Reproduce:**
1. Open /signup
2. Enter `<script>alert(1)</script>` in email or name fields
3. Submit the form

**Actual Result:** Alert dialog appears indicating script executed on page.
**Expected Result:** Input should be sanitized; scripts must not execute.
**Severity:** Critical
**Priority:** P0
**Attachments:** evidence/screenshots/BUG-006.png

**Suggested Fix:** Sanitize user inputs on server-side and escape output in templates.
