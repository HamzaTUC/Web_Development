from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index_1():
	return render_template("index_1.html")


@app.route("/hello", methods= ["POST"])
def hello():
	if request.form.get("password")== "hamza05":
		name= request.form.get("name")
		return render_template("hello.html", name=name)
	else:
		return "please enter a correct password"	