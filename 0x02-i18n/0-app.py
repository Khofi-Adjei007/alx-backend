#!/usr/bin/env python3
"""
Task 0: Basic Flask Application
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the default route.

    Returns:
        The rendered template for the homepage.
    """
    return render_template("0-index.html")

if __name__ == "__main__":
    # Run the Flask development server with debug mode enabled.
    app.run(debug=True)
