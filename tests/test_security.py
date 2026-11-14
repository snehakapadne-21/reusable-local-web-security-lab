import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["WTF_CSRF_ENABLED"] = False

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_security_headers(client):
    response = client.get("/")
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"


def test_search_escapes_html(client):
    response = client.get("/search?q=<script>alert(1)</script>")
    assert response.status_code == 200
    assert b"&lt;script&gt;" in response.data


def test_search_rejects_long_input(client):
    response = client.get("/search?q=" + "a" * 101)
    assert response.status_code == 400


def test_profile_requires_login(client):
    response = client.get("/profile")
    assert response.status_code == 302


def test_login_and_logout(client):
    response = client.post(
        "/login",
        data={
            "username": "demo",
            "password": "ChangeMe-Local-Only!"
        }
    )
    assert response.status_code == 302

    response = client.get("/profile")
    assert response.status_code == 200

    client.get("/logout")
    response = client.get("/profile")
    assert response.status_code == 302
