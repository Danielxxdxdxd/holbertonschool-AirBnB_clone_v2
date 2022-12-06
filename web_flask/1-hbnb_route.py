#!/usr/bin/python3
'''Flask WSGI for multiple routes'''


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''First function. Prints on /'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def just_hbnb():
    '''Second function. Prints on /hbnb'''
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
