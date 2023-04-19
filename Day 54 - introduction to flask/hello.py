from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello, world!</h2>'


@app.route('/about')
def about():
    return "this is the about page"


if __name__ == '__main__':
    app.run()

