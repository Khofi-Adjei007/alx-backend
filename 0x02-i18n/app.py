#!/usr/bin/env python3

"""
A Basic Flask app with internationalization support.
"""

import pytz
from typing import Union, Dict
from flask_babel import Babel, format_datetime
from flask import Flask, render_template, request, g

class Config:
    """
    Represents a Flask Babel configuration.

    Attributes:
        LANGUAGES (list): List of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

# Sample users data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[Dict, None]:
    """
    Retrieve a user based on a user ID from the query parameters.

    Returns:
        Union[Dict, None]: The user dictionary if found, None otherwise.
    """
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None)
    return None

@app.before_request
def before_request() -> None:
    """
    Perform routines before each request's resolution.

    This sets the global user object for the request.
    """
    user = get_user()
    g.user = user

@babel.localeselector
def get_locale() -> str:
    """
    Retrieve the locale for the web page.

    Checks the URL parameter first, then the user's locale,
    followed by the Accept-Language header.

    Returns:
        str: The best match for the requested languages.
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    locale = query_table.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    user_details = getattr(g, 'user', None)
    if user_details and user_details['locale'] in app.config["LANGUAGES"]:
        return user_details['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']

@babel.timezoneselector
def get_timezone() -> str:
    """
    Retrieve the timezone for the web page.

    Checks the URL parameter first, then the user's timezone.

    Returns:
        str: The appropriate timezone.
    """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']

@app.route('/')
def get_index() -> str:
    """
    Render the home/index page.

    Returns:
        str: The rendered template for the homepage.
    """
    g.time = format_datetime()
    return render_template('index.html')

if __name__ == '__main__':
    # Run the Flask development server.
    app.run()
