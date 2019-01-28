from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask('FlaskApp')

@app.route("/")
def Index():
    return "Index"

@app.route("/helloworld")
def hello():
    return "Hello World!"

@app.route("/members")
def memebers():
    return "Members"

@app.route("/render")
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run()
