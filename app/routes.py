from flask import Blueprint, request, session, redirect, url_for
from flask import render_template_string, abort
import os

bp = Blueprint("main", __name__)


@bp.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    return response


@bp.route("/")
def home():
    return """
    <h1>Local Web Security Lab</h1>
    <form action="/search">
        <input name="q" maxlength="100">
        <button>Search</button>
    </form>
    <a href="/login">Login</a>
    """


@bp.route("/search")
def search():
    query = request.args.get("q", "")

    if len(query) > 100:
        abort(400)

    return render_template_string(
        "<h2>Search result: {{ query }}</h2>",
        query=query
    )


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        expected_user = os.environ.get("DEMO_USERNAME", "demo")
        expected_password = os.environ.get(
            "DEMO_PASSWORD", "ChangeMe-Local-Only!"
        )

        if username == expected_user and password == expected_password:
            session["user"] = username
            return redirect(url_for("main.profile"))

        return "Invalid login", 401

    return """
    <form method="POST">
    <input type="hidden" name="csrf_token" value="{{ csrf_token() }}">
    <input name="username" placeholder="Username">
    <input name="password" type="password" placeholder="Password">
    <button type="submit">Login</button>
</form>
        <input name="password" type="password" placeholder="Password">
        <button type="submit">Login</button>
    </form>
    """


@bp.route("/profile")
def profile():
    if "user" not in session:
        return redirect(url_for("main.login"))

    return f"Signed in as {session['user']}"


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.home"))
