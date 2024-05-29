#!/usr/bin/env python3
"""Module to create a login system outside the project's scope"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _


app = Flask(__name__)


class Config:
    """Class configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """Function to let a user login"""
    try:
        return users.get(int(login_as))
    except Exception:
        return


@babel.localeselector
def get_locale():
    """Function to determine the best match with the supported languages"""
    locale = request.args.get("locale")
    if locale:
        return locale
    if g.get("user") and g.user["locale"] in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.before_request
def before_request():
    """Function to use app.before_request to enable execution before others"""
    g.user = get_user(request.args.get("login_as"))


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """Function to print Hello world"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
