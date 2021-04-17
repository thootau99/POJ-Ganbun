import os
from db import MongoGo
from flask import Flask, render_template, request, send_from_directory
import json
# from flask_cors import CORS, cross_origin

from ganbun import input
from bson.objectid import ObjectId


app = Flask(__name__, static_url_path='', static_folder='frontend/build')
# cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

client = MongoGo()

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

@app.route("/api/v1/chhoe")
# @cross_origin()
def chhoe():
    result, _ = input(request.args.get('bun'))
    return result

@app.route("/api/v1/dict")
def chhoeDict():
	keyword = request.args.get('keyword')
	if request.args.get('blur') is None:
		blur = True
	else:
		blur = False

	return json.dumps(client.find(keyword, blur), ensure_ascii=False)

if __name__ == '__main__': app.run(debug=True)