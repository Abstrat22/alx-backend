#!/usr/bin/env python3
"""
Flask app for rendering an HTML template with language support, incorporating user data and handling user login.
"""
from flask import Flask, render_template, request, g  # Importing necessary modules
from flask_babel import Babel  # Importing Babel for language support

# Dictionary containing user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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

def get_user():
    """
    Returns a user dictionary or None if the ID value can't be found or if 'login_as' URL parameter was not found.
    """
    id = request.args.get('login_as', None)  # Getting the 'login_as' parameter from the URL
    if id is not None and int(id) in users.keys():  # Checking if the provided ID exists in the users dictionary
        return users.get(int(id))  # Return the user if found
    return None  # Return None if the user is not found

@app.before_request
def before_request():
    """
    Adds the user to flask.g if the user is found.
    """
    user = get_user()  # Getting the user based on the ID from the URL
    g.user = user  # Adding the user to the flask.g context

@babel.localeselector
def get_locale():
    """
    Selects and returns the best language match based on supported languages.
    """
    loc = request.args.get('locale')  # Checking for the 'locale' parameter in the request
    if loc in app.config['LANGUAGES']:  # If the provided language is supported
        return loc  # Return the specified language
    return request.accept_languages.best_match(app.config['LANGUAGES'])  # Otherwise, return the best match based on the accepted languages

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the index HTML template.
    """
    return render_template('5-index.html')  # Rendering the '5-index.html' template

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)  # Running the app on port 5000 and allowing debugging

