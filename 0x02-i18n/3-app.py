#!/usr/bin/env python3
"""
Flask app for rendering an HTML template with language support.
"""
from flask import Flask, render_template, request
from flask_babel import Babel  # Importing Babel for language support


class Config(object):
    """
    Configuration class for the Flask app.
    """
    LANGUAGES = ["en", "fr"]  # Supported languages for localization
    BABEL_DEFAULT_LOCALE = "en"  # Default language for the app
    BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone for the app


app = Flask(__name__)  # Initializing the Flask app
app.config.from_object(Config)  # Configuring the app with the Config class
babel = Babel(app)  # Initializing Babel for the app


@babel.localeselector
def get_locale():
    """
    Selects and returns the best language match based on supported languages.
    """

    # Selecting the best language for the request
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the index HTML template.
    """

    # Rendering the '3-index.html' template
    return render_template('3-index.html')


if __name__ == "__main__":
    # Running the app on port 5000 and allowing debugging
    app.run(port="5000", host="0.0.0.0", debug=True)
