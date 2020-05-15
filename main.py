from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/education")
def education():
	return render_template("education.html")

@app.route("/gallery")
def gallery():
	return render_template("gallery.html")

if __name__ == "__main__":
	app.run()