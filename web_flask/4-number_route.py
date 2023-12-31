#!/usr/bin/python3
""" starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ index route definition
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb route definition
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """ display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space)
    """
    return 'C ' + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text="is cool"):
    """ display “Python ”, followed by the value of the text variable
        (replace underscore _ symbols with a space)
    """
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ display “n is a number” only if n is an integer
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
