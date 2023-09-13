from flask import Flask
from osuapi import osuauth
from flask_cors import CORS
from flask.json import jsonify


import sys



server = Flask(__name__)


CORS(server, origins=['http://localhost:3000'])

@server.route('/')
def index():
    data = {'message': 'This is the authapi endpoint'}
    return jsonify(data)

server.register_blueprint(osuauth.auth)




if __name__ == '__main__':
    server.run(debug=True)
  