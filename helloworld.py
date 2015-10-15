from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
	return 'Hello World!'
		
@app.route('/index')
def index():
	return "Hello Index"
		
if __name__ == "__main__":
	app.run()
	