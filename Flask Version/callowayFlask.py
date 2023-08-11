from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Hello"

if __name__ == "__main__":
    app.run()