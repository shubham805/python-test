# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("Console write")
    print(request.headers)
    return "<p>Hello, World!</p>"

app.run(host='0.0.0.0', port=2000)
