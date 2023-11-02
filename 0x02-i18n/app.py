#!/usr/bin/env python3
"""
Flask app for rendering an HTML template with language and timezone support, and user data handling.
"""
import locale  # Importing the locale module for localization
from flask import Flask, render_template, request, g  # Importing necessary modules
from flask_babel import Babel  # Importing Babel for language and timezone support
from datetime import timezone as tmzn, datetime  # Importing necessary modules for date and time
from pytz import timezone  # Importing timezone from pytz module
import pytz.exceptions  # Importing exceptions from pytz module
from typing import Dict, Union  # Importing type hints for better code readability and maintainability

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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[Dict, None]:
    """
    Returns a user dictionary or None if the ID value can't be found or if the 'login_as' URL parameter was not found.
    """
    id = request.args.get('login_as', None)  # Getting the 'login_as' parameter from the URL
    if id and int(id) in users.keys():  # Checking if the provided ID exists in the users dictionary
        return users.get(int(id))  # Return the user if found
    return None  # Return None if the user is not found

@app.before_request
def before_request():
    """
    Adds the user to flask.g if the user is found and sets the current time and date.
    """
    user = get_user()  # Getting the user based on the ID from the URL
    g.user = user  # Adding the user to the flask.g context
    time_now = pytz.utc.localize(datetime.utcnow())  # Getting the current time in UTC
    time = time_now.astimezone(timezone(get_timezone()))  # Converting the time to the user's timezone
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))  # Setting the locale for the app
    fmt = "%b %d, %Y %I:%M:%S %p"  # Date and time format
    g.time = time.strftime(fmt)  # Setting the formatted time in the flask.g context

@babel.localeselector
def get_locale():
    """
    Selects and returns the best language match based on supported languages, prioritizing user locale and request headers.
    """
    loc = request.args.get('locale')  # Checking for the 'locale' parameter in the request
    if loc in app.config['LANGUAGES']:  # If the provided language is supported
        return loc  # Return the specified language
    if g.user:  # If user is found in the context
        loc = g.user.get('locale')  # Get the user's preferred language
        if loc and loc in app.config['LANGUAGES']:  # If the user's preferred language is supported
            return loc  # Return the user's preferred language
    loc = request.headers.get('locale', None)  # Checking for the 'locale' parameter in the request headers
    if loc in app.config['LANGUAGES']:  # If the language in the request headers is supported
        return loc  # Return the language from the request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])  # Otherwise, return the best match based on the accepted languages

@babel.timezoneselector
def get_timezone():
    """
    Selects and returns the appropriate timezone, prioritizing user timezone and request parameters.
    """
    tzone = request.args.get('timezone', None)  # Checking for the 'timezone' parameter in the request
    if tzone:
        try:
            return timezone(tzone).zone  # Return the timezone if it exists
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:  # If user is found in the context
        try:
            tzone = g.user.get('timezone')  # Get the user's preferred timezone
            return timezone(tzone).zone  # Return the user's preferred timezone if it exists
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    dflt = app.config['BABEL_DEFAULT_TIMEZONE']  # Get the default timezone from the app configuration
    return dflt  # Return the default timezone

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles the / route and renders the index HTML template.
    """
    return render_template('5-index.html')  # Rendering the '5-index.html' template

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)  # Running the app on port 5000 and allowing debugging

