#!/usr/bin/python3
"""
Module 1-hello_route.Script that start a
Flask web application Test on tab:python3
-m web_flask.1-hello_route
On another tab:curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


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


@app.route("/c/<text>")
def c_is_fun(text):
    """
    Display C then text variable
    if text valueless return 404
    """
    return ("C {}".format(text.replace('_', ' ')))


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """
    display python, the text value
    return is cool as text default
    """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route("/number/<int:n>")
def is_a_number(n):
    """
    display n is a number only
    if n is an integer
    """
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>")
def number_temp(n):
    """
    display a HTML page
    H1 tag Number: n
    only if n is an int
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def even_or_odd(n):
    """
    display Number: n is even or odd
    """
    number = "even" if (n % 2 == 0) else "odd"
    return render_template(6-number_odd_or_even.html, number=number, n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
