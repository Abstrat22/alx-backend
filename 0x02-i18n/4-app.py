#!/usr/bin/env python3
"""
Flask app for rendering an HTML template with language support, allowing the user to set the language via query parameter.
"""
from flask import Flask, render_template, request  # Importing necessary modules
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
    Selects and returns the best language match based on supported languages or the user-provided query parameter.
    """
    loc = request.args.get('locale')  # Checking for the 'locale' query parameter in the request
    if loc in app.config['LANGUAGES']:  # If the provided language is supported
        return loc  # Return the specified language
    return request.accept_languages.best_match(app.config['LANGUAGES'])  # Otherwise, return the best match based on the accepted languages


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the index HTML template.
    """
    return render_template('4-index.html')  # Rendering the '4-index.html' template


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)  # Running the app on port 5000 and allowing debugging

