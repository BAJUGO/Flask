from flask import Flask, render_template, request, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)


@app.route('/filters')
def filters():
    text = "hello BEautiful world!"
    return render_template('filters.html', text=text)


@app.route('/test_route')
def test():
    value = 'This'
    result = round(5 + 5.5)
    my_dictionary = [10,20,30,40]
    return render_template('test.html', value=value, result=result, list = my_dictionary) # On the left side the thing that in the HTML, so we do a referring, IDK.


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


@app.route("/itdoesntimportentwhatwrittenthere", methods=['GET', 'POST']) # Look at index.html
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



@app.route('/redirect')
def handle_redirect():
    return redirect(url_for('about')) # It is obvious what it does, but just for you to understand: it redirects to the about page



@app.template_filter('reverse_string')
def reverse(s):
    return s[::-1]


@app.template_filter('repeat')
def repeat(s, times=2):
    return f"{s * times}"


@app.template_filter('alternate_case')
def alt(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])


if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=True)