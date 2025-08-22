from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)


@app.route("/", methods=['GET', 'POST'])
@app.route("/home")
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    response = make_response('Hello world')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response

@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("about.html")


@app.route('/greet/<name>') # By this <name> we create a new variable
def greet(name):
    return f"hello, {name}" # If you use template, the curl request is large because it shows all the HTML code


@app.route('/add/<int:number1>/<int:number2>') # We could write {int(number1) + int(number2)}, but this is easier
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


@app.route('/handle_url_params')
def handle_params():
    # if 'greeting' in request.args.keys() and 'name" in request.args.keys():
    greeting = request.args['greeting']
    name = request.args.get('name', 'guest')  # It is better to write args.get because it won't raise an error
    return f"{name}, {greeting}"



if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)