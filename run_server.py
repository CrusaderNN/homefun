#adding comment
import RPIO
from flask import Flask
from flask import render_template

import shutil

import requests

url = 'http://example.com/img.png'
response = requests.get(url, stream=True)
with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

app = Flask(__name__)
RPIO.setup(14, RPIO.OUT)
@app.route("/on")
def ledon():
	RPIO.output(14, True)	
	return render_template('page.html')

@app.route("/off")
def ledoff():
	RPIO.output(14, False)	
	return render_template('page.html')

@app.route("/")
def hello():
	return render_template('page.html')


if __name__ == "__main__":
    app.run()