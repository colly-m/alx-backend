#!/usr/bin/env python3
"""Module to create a single route to an html in template"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    """Function to print Hello world"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
