#!/usr/bin/python3
"""
task 1
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

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
