from flask import Flask

myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "Hello World"
@myapp.route("/sumonhlaing")
def smh():
    return "Su Mon Hlaing"
if __name__ == "__main__":
    myapp.run()
