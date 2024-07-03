#!/usr/bin/env python3

"""
Task 4: Force Locale with URL Parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """
    Configuration class for the Flask application.

    Attributes:
        DEBUG (bool): Enable or disable debug mode.
        LANGUAGES (list): Supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale
        for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone
        for the application.
    """
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

# Initialize Babel for internationalization support
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """
    Retrieve the locale for the web page, checking URL parameters first.

    Returns:
        str: The locale to use for the request.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Render the default route.

    Returns:
        str: The rendered template for the homepage.
    """
    return render_template("4-index.html")

# Uncomment the line below and comment out the @babel.localeselector decorator
# to use the alternative method of initializing Babel with a locale selector.
# Note: Uncommenting will result in the following error:
# AttributeError: 'Babel' object has no attribute 'localeselector'
# babel.init_app(app, locale_selector=get_locale)

if __name__ == "__main__":
    # Run the Flask development server.
    app.run()
