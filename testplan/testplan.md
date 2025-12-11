# Test Plan — Web App Functional QA (Demo Web App)

**Project:** Demo Web App Functional QA
**Scope:** Login, Signup, Profile (if implemented), Dashboard, Notifications (if any), Search/Filters (if any), Settings (if any)
**Test Environment:** Localhost http://127.0.0.1:5000, Chrome (latest), Windows 10
**Test Types:** Functional, Negative, Boundary, Security (basic), Usability, Responsive, Exploratory
**Entry Criteria:** App running locally, test data available (able to sign up), environment stable
**Exit Criteria:** All P0/P1 test cases executed; no critical (P0) open; execution summary and evidence delivered
**Roles:** Tester: You; Developer: (TBD)

## Deliverables
- Test Plan (this document)
- Test Cases (.xlsx)
- Bug Reports (CSV + GitHub Issues)
- Evidence (Screenshots / Short videos)
- Execution Summary

## Test Schedule
- Day 1: Setup, Test Plan, Test Case creation
- Day 2: Execute Signup & Login test cases
- Day 3: Execute Dashboard & Session tests, exploratory testing
- Day 4: Collate evidence, prepare execution summary and bug reports
- Day 5: Regression verification after fixes

## Risks & Assumptions
- External integrations like email may not be available locally (affects forgot-password workflows)
- App is a demo; some features may be intentionally minimal

## Test Environment Setup
1. Ensure Flask app running: `python app.py`
2. Chrome browser, devtools available
3. Create folders: `evidence/screenshots`, `evidence/videos`

## Reporting & Communication
- Use GitHub Issues for bug tracking or import CSV into Jira.
- Attach screenshots/videos to tickets.
- Daily stand-up style updates in README.

