import RPIO
from flask import Flask
from flask import render_template

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
