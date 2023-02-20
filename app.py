from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/api/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        data = request.json
        name = data.get("name")
        greeting = f"Hello, {name}!"
        return {"greeting": greeting}
    else:
        return {"message": "Please use a POST request to submit data."}


if __name__ == "__main__":
    app.run(debug=True)
