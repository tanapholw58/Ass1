from flask import Flask
from flask_restful import Resource , Api,reqparse
from datetime import date, datetime
import json ,time 

app = Flask (__name__)
api = Api(app) 

parser = reqparse.RequestParser()
parser.add_argument('dob')

def calculate_age(born):
		today = date.today()
		return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class Hello(Resource):
	def post(self): 
		args = parser.parse_args()
		birthdate = args['dob']
		dob = calculate_age(datetime.strptime(birthdate, '%d-%m-%Y').date())
		return {"birthdate":birthdate, "Age":dob}

api.add_resource(Hello,'/age')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0',port=5500)
