#!/usr/bin/env python3
"""Module to instatiate Babel obj into the app"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """Class configurations"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Function to determine the best match with the supported languages"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """Function to print Hello world"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
