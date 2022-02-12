from flask import Flask, jsonify, request
try:
	import jwt
	list_bearer = True
except:
	list_bearer = False

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def hello():
	return "Hello World from some pig!\n"

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
	user = request.environ.get('REMOTE_USER', 'No REMOTE_USER')
	return f'<h1>{user}</h1>'

if list_bearer:
	@app.route("/bearer")
	def bearer_decode():
		bearer_token = 'No token found'
		auth_header = request.headers.get('Authorization')
		if auth_header and 'Bearer ' in auth_header:
			bearer_token = auth_header.split(' ')[1]
			#return f'<h1>{bearer_token}</h1>'
			payload = jwt.decode(bearer_token, options={'verify_signature': False})
			hdr = jwt.get_unverified_header(bearer_token)
			return jsonify({'header': hdr, 'payload': payload})
		return f'<h1>{bearer_token}</h1>'

if __name__ == "__main__":
	app.run()
