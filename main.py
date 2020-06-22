from flask import Flask
from flask import render_template
from forms import MyForm
from flask_wtf.csrf import CSRFProtect

import os

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "secretkey"
app.config['WTF_CSRF_SECRET_KEY'] = "secretkey"
csrf.init_app(app)



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

@app.route("/contact", methods=['GET','POST'])
def contact():
	myform = MyForm()
	if myform.validate_on_submit():
		return redirect(url_for(''))
	return render_template("contact.html", myform = myform)

	


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
	

