#!/usr/bin/env python3
"""
A simple Flask application that renders an HTML template.
"""
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Route for the root URL ('/')
@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles the root route, rendering the '0-index.html' template
    """
    return render_template('0-index.html')

# Run the Flask application if the script is executed directly
if __name__ == "__main__":
    # Run the app on port 5000, allowing access from all network interfaces, and with debugging enabled
    app.run(port="5000", host="0.0.0.0", debug=True)

