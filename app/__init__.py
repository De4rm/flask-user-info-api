from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/whoami')
def whoami():
	language = str(request.accept_languages).split(",")[0]
	user_agent = request.headers.get('User-Agent')
	index_start = user_agent.index("(") + 1
	index_end = user_agent.index(")")
	platform = user_agent[index_start:index_end]
	return jsonify({ "ipaddress" : request.remote_addr, 
					 "language" : language,
					 "software" : platform})