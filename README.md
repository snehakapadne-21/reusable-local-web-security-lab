# Reusable Local Web-Security Lab

A reusable defensive training project for a web application running on localhost. Includes a Flask demo app, manual checklist, remediation notes, automated regression tests, and evidence templates.

**Safety scope:** Test only this included app on localhost or systems you own / have written permission to test. Do not scan public websites. This is an educational demo, not a production-ready application.

## Contents
- `app/`: demo application
- `tests/`: automated regression tests
- `checklist/`: manual test checklist
- `remediation/`: example findings and fixes
- `evidence/`: blank results template (tests are Not Run until executed)
- `docs/`: setup, workflow, and limitations
- `Dockerfile`, `docker-compose.yml`, `requirements.txt`: reproducible setup

## Requirements
Python 3.11+ and pip, or Docker Desktop with Compose.

## Run with Python
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m flask --app app run --host 127.0.0.1 --port 5000
```
Open `http://127.0.0.1:5000`.

## Run with Docker
```bash
docker compose up --build
```
Open `http://127.0.0.1:5000`; stop with `docker compose down`. The host port is bound to localhost.

## Run regression tests
```bash
pip install -r requirements.txt
pytest -q
```
Tests use Flask's in-process test client and do not scan an external host.

## Demo login
Defaults: `demo` / `ChangeMe-Local-Only!`. These are for local training only. Never reuse them or expose the demo app publicly.

## Workflow
1. Confirm scope and authorization.
2. Start the local app.
3. Complete the manual checklist and capture evidence.
4. Run regression tests.
5. Record each finding, impact, remediation owner, and retest result.
6. Mark outcomes Pass, Fail, or Not Run honestly.

## Limitations
This small app is not a full vulnerability scanner and does not cover every OWASP category. The evidence template is not proof of execution. Fill it only after running the checks.

## References
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- Flask documentation: https://flask.palletsprojects.com/
