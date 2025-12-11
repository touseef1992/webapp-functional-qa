# BUG-004 — Session visible after logout via back button (Major)

**Summary:** After logout, pressing browser back button shows dashboard content.

**Environment:** Local http://127.0.0.1:5000, Chrome

**Steps to Reproduce:**
1. Login with user account
2. Click logout
3. Press browser back button

**Actual Result:** Dashboard content becomes visible without prompting to login.
**Expected Result:** Should redirect to login or show logged-out state; cache-control headers should prevent cached content display.
**Severity:** Major
**Priority:** P1
**Attachments:** evidence/videos/BUG-004.mp4

**Suggested Fix:** Implement cache-control headers and proper session invalidation.
