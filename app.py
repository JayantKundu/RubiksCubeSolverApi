
from flask import Flask, request
import kociemba
app=Flask(__name__)


@app.route('/')
def starting():
	return "Welcome to my rubiks cube solver api"
	

@app.route('/cubeMap/<user_id>', methods = ['GET'])
def user(user_id):
	if request.method == 'GET':
		try:
			a = kociemba.solve(user_id)
		except:
			a = "an error occured"
		
		return a



if __name__ == "__main__":
	# app.run(port=8080)
	app.run()