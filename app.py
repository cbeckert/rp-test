from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
    return "<h1 style='color:blue;'>Hallo wereld</h1>"

if __name__ == "__main__":
    app.run()
