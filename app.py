from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from unicodedata import digit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/greet/<name>') # By this <name> we create a new variable
def greet(name):
    return f"hello, {name}"


@app.route('/add/<int:number1>/<int:number2>') # We could write {int(number1) + int(number2)}, but this is easier
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)