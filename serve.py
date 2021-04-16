import os
from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS, cross_origin

from ganbun import input

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

@app.route("/api/v1/chhoe")
@cross_origin()
def chhoe():
    result, _ = input(request.args.get('bun'))
    return result

if __name__ == '__main__': app.run(debug=True)