from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
import os
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)

from pymongo import MongoClient
client = MongoClient(os.getenv('MONGO_HOST','localhost'), int(os.getenv('MONGO_PORT', '27017')))
db = client.stuffes

class Stuff(Resource):
	def get(self):
		return dumps(db.stuff.find())
    	def post(self):
		db.stuff.insert(request.json)

api.add_resource(Stuff, '/stuff') 


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port='5002')
