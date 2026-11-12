# Security Remediation Examples

## 1. Missing Security Headers

Problem:
Important HTTP security headers are missing.

Impact:
The application may be exposed to browser-based risks.

Remediation:
Configure appropriate security headers in Flask responses.

Verification:
Check response headers after applying the fix.

## 2. Excessive Input Length

Problem:
Users can submit very long search inputs.

Impact:
Unnecessary processing and resource usage.

Remediation:
Set a maximum input length of 100 characters.

Verification:
Confirm inputs above 100 characters return HTTP 400.

## 3. Unescaped User Input

Problem:
User input may be displayed without safe escaping.

Impact:
HTML or script content could be interpreted by the browser.

Remediation:
Use Jinja autoescaping and avoid unsafe HTML rendering.

Verification:
Confirm HTML-like input is displayed as text.

## 4. Unprotected Profile Page

Problem:
Profile page can be accessed without authentication.

Impact:
Unauthorised access to protected content.

Remediation:
Check the login session before displaying the profile.

Verification:
Confirm unauthenticated requests are redirected to login.

## 5. Regression Testing

After every fix:
- Run the automated test suite.
- Check the affected functionality.
- Record actual results.
- Document unresolved limitations.

Scope: Educational localhost application only.
