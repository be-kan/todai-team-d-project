from flask import Flask, render_template, request
import urllib
import json

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hikakin')
def kikakin():
    return render_template('hikakin.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
