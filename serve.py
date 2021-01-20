import os
from flask import Flask, render_template, request
from ganbun import input

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", message="Hello Flask!");   

@app.route("/chhoe")
def chhoe():
    return input(request.args.get('bun'))

if __name__ == '__main__': app.run(debug=True)