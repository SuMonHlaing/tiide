from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"
@app.route("/sumonhlaing")
def smh():
    return "Su Mon Hlaing"
if __name__ == "__main__":
    app.run()
