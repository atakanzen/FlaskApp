from flask import Flask
from flask import request
from flask import render_template
from forms import MyForm
from flask_wtf.csrf import CSRFProtect
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
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

@app.route("/contact", methods=['POST','GET'])
def contact():
	myform = MyForm()
	if request.method == 'POST':
		if myform.validate_on_submit():
			message = Mail(
			from_email= myform.email.data,
			to_emails='atakanzzengin@gmail.com',
			subject=myform.name.data + 'wants to contact Atakan',
			plain_text_content=myform.message.data)
			try:
				sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
				response = sg.send(message)
				# print(response.status_code)
				# print(response.body)
				# print(response.headers)
			except Exception as e:
				print(e)
				# print(e.message)
	return render_template("contact.html", myform = myform)

	


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
	

