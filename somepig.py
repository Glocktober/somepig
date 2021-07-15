from flask import Flask, jsonify, request

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def hello():
	return "Hello World!\n"

@app.route("/json")
def jello():
	return jsonify({'hello': 'world'})

@app.route("/env")
def getEnv():
	results = {}
	evars = []
	for key in request.environ.keys():
		evars.append(key)
		if key[0].isupper():
			results.update({ key : request.environ.get(key) })
	results.update({ 'allkeys' : evars})
	return jsonify(results)

@app.route("/hdr")
def getHdrs():
	results = {}
	for key in request.headers.keys():
		if key[0].isupper():
			results.update({ key : request.headers.get(key) })
	return jsonify(results)

@app.route("/whoami")
def whoamI():
	user = request.environ.get('REMOTE_USER')
	return f'<h1>{user}</h1>'

if __name__ == "__main__":
	app.run()
