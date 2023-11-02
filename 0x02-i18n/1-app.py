#!/usr/bin/env python3
"""
A simple Flask application that renders an HTML template.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Config class for the Flask app.
    """
    LANGUAGES = ["en", "fr"]  # Supported languages for localization
    BABEL_DEFAULT_LOCALE = "en"  # Default language for the app
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone for the app


app = Flask(__name__)  # Initializing the Flask app
app.config.from_object(Config)  # Configuring the app with the Config class
babel = Babel(app)  # Initializing Babel for the app


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the index HTML template.
    """
    return render_template('1-index.html')  # Rendering the '1-index.html' template


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)  # Running the app on port 5000 and allowing debugging

