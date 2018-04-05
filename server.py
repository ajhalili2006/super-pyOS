# server.js
# where your node app starts

# init project
from flask import Flask, jsonify, render_template, request
application = Flask(__name__)


# I've started you off with Flask, 
# but feel free to use whatever libs or frameworks you'd like through `.requirements.txt`.

@application.route("/")
def hello():
    return render_template('index.html')

# Simple in-memory store
dreams = [
  'Find and count some sheep',
  'Climb a really tall mountain',
  'Wash the dishes',
]

@application.route('/dreams', methods=['GET'])
def get_dreams():
    return jsonify(dreams)

# // could also use the POST body instead of query string: http://expressjs.com/en/api.html#req.body
@application.route('/dreams', methods=['POST'])
def add_dream():
    return jsonify(dreams)
  
  
# listen for requests :)
if __name__ == "__main__":
    from os import environ
    application.run(host='0.0.0.0', port=int(environ['PORT']))