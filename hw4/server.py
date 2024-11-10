from flask import Flask, jsonify, request
from dotenv import dotenv_values

from controllers import operation


app = Flask(__name__)


@app.route("/")
def server_info() -> str:
    return "My server"


@app.route("/author")
def author():
    author = {
        "name": "Nikita",
        "course": 5,
        "age": 22,
    }
    return jsonify(author)


@app.route("/sum")
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})


def get_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return int(config["PORT"])
    return 5000


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=get_port())
