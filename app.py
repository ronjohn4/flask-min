from flask import Flask

app = Flask(__name__)


@app.route('/')
def route_root():
    return "Endpoints are /, /hi, /bye"


@app.route('/hi')
def route_hi():
    return "Hi there"


@app.route('/bye')
def route_bye():
    return "see ya"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
