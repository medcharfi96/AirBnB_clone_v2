#!/usr/bin/python3
"""
task 3
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    return : hello HBNb
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def only_HBNB():
    """
    return : hello HBNb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_replace_text(text):
    """
    return : c is text
    """
    text_to_replace = text.replace("_", " ")
    return "C {}".format(text_to_replace)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python_replace_text(text='is cool'):
    """
    return : Python is text
    """
    text_to_replace = text.replace("_", " ")
    return 'Python ' + text_to_replace

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
