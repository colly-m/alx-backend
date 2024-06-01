#!/usr/bin/env python3
"""Module to create a login system outside the project's scope"""
from flask import Flask, render_template, request, g
from crypt import methods
import pytz
from flask_babel import Babel, gettext as _
import requests
import babel
from email import header


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
    user = request.args.get("login_as")
    if user:
        language = user.get(int(user)).get("locale")
        if language in app.config["LANGUAGES"]:
            return language
    header = request.header.get("locale")
    if header:
        return header
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.before_request
def before_request():
    """Function to use app.before_request to enable execution before others"""
    g.user = get_user(request.args.get("login_as"))


@babel.timezoneselector
def get_timezone():
    """Function to get timezones and default to UTC"""
    try:
        timezone = request.args.get("timezone")
        if timezone:
            return pytz.timezone(timezone)
        user = request.args.get("login_as")
        if user:
            timezone = users.get(int(user)).get('timezone')
            if timezone:
                return pytz.timezone(timezone)
        timezone = request.headers.get("timezone")
        if timezone:
            return pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        return app.config.get('BABEL_DEFAULT_TIMEZONE')
    return app.config.get('BABEL_DEFAULT_TIMEZONE')


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """Function to print Hello world"""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(debug=True)
