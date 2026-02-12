from flask import Flask, request, jsonify

from core.app.greet import make_greeting

app = Flask(__name__)

@app.get("/hello")
def hello():
    name = request.args.get("name")
    greeting = make_greeting(name)
    return jsonify(message=greeting.message)


if __name__ == "__main__":
    app.run(debug=True)