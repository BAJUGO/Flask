from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/blog/<int:id>")
def blog_post(id):
    return render_template("blog_post.html")



@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)