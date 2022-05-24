from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"
@app.route('/davaa')
def davaa():
    return "Hello davaa"


if __name__ == '__main__':
    app.run(debug=True)