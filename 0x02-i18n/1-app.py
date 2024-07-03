#!/usr/bin/env python3

"""
Task 0: Basic Flask Application with
Babel for Internationalization
"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """
    Configuration class for the Flask application.

    Attributes:
        LANGUAGES (list): Supported languages.
        BABEL_DEFAULT_LOCALE (str): Default
        locale for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default
        timezone for the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

# Initialize Babel for internationalization support
babel = Babel(app)

@app.route('/')
def index():
    """
    Render the default route.

    Returns:
        The rendered template for the homepage.
    """
    return render_template("1-index.html")

if __name__ == "__main__":
    # Run the Flask development server with debug mode enabled.
    app.run(debug=True)
