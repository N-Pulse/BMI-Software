from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Here is the application environment!"

app.run(debug=True)

