from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def test_project():
    return "WELCOME TO THE PROJECT..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(8080), debug=False)