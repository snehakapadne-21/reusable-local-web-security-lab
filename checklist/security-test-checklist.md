# Security Test Checklist

## Scope
- [ ] Run tests only on localhost.
- [ ] Confirm the application is running.

## Security Headers
- [ ] Check X-Content-Type-Options.
- [ ] Check X-Frame-Options.
- [ ] Check Referrer-Policy.
- [ ] Check Content-Security-Policy.

## Input Validation
- [ ] Submit normal search input.
- [ ] Submit HTML-like input.
- [ ] Check that input over 100 characters is rejected.

## Authentication
- [ ] Open profile without login.
- [ ] Try valid demo login.
- [ ] Check profile after login.
- [ ] Test logout.

## Evidence
- [ ] Record actual test results.
- [ ] Save screenshots where possible.
- [ ] Document issues and fixes.

Only test this local educational application.
