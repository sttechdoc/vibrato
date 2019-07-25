from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def test_project():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(8080), debug=False)