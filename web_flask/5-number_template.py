#!/usr/bin/python3
"""
This script display “Hello HBNB!” on '/' and
“HBNB” on /hbnb route
"C <text>" on /c/ rourte and the text variable
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main_page():
    """Return “Hello HBNB!” on the console"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Return "HBNB" on the console on /hbnb"""
    return "HBNB"


@app.route('/c/<text>')
def display_text(text):
    """Return "C" + <text> variable on /c/"""
    new_string = text
    if '_' in new_string:
        new_string = text.replace('_', ' ')
    return 'C {}'.format(new_string)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def display_text_default(text):
    """Return "Python" with the default value is cool"""
    new_string = text
    if '_' in new_string:
        new_string = text.replace('_', ' ')
    return 'Python {}'.format(new_string)


@app.route('/number/<int:n>')
def display_int(n):
    """Return n is a number only if n is type int"""
    if type(n) is int:
        return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def display_html(n):
    """Display a html page only if n is type int"""
    if type(n) is int:
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
