from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the main page"

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        
    return render_tempalte()

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run()

