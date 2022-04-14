#!/usr/bin/python3
"""Script that start a Flask web application """

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map..strict_slashes = False

@app.route("/")
def hello_hbnb():
    """
    route function 
    that displays string on url page
    """
    return ("Hello HBNB!")

@app.route("/hbnb")
def hbnb():
    """ 
    displays HBNB when /hbnb
    is used in url
    """
    return ("HBNB")

@app.route("/c/<text")
def c_is_fun(text):
    """
    Displays C followed by value of text
    replace _ sysmbols with a space
    without the text it returns 404
    """
    return ("C {}".format(text.replace('_', ' ')))

@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """
    display "Python" followed by text variable
    text variable. replace _ with space
    The default value of text is "is cool"
    """
    return ("Python {}".format(text.replace('_', ' ')))

@app.route("/number/<int:n>")
def is_a_number(n):
    """
    display n is a number
    only if n is an integer
    """
    return ("{} is a number".format(n))

@app.route("/number_template/<int:n>")
def number_template(n):
    """
    display a HTML page only
    if n is an int
    H1 tag: "Number: n" inside the body tag
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
