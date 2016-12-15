#/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hell-o World!"

if __name__ == "__main__":
    app.run(host='pictaricta.com')
