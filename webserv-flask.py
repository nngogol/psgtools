#!/usr/bin/python3
'''
	pip install Flask
'''

from flask import Flask, request, jsonify; app = Flask(__name__)

@app.route('/exec', methods=['GET', 'POST'])
def exec(): return jsonify({'input_json': request.json, 'output': str(eval(request.json['i']))})
@app.route('/', methods=['GET', 'POST'])
def index():
	ijson = request.json
	method = request.method
	print(f'{ijson=}')
	print(f'{method=}')
	
	return jsonify({'input_json': ijson, 'method': method})

if __name__ == '__main__':
	app.run(debug=True, port=5000, host='127.0.0.1')