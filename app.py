from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>This is homepage</h1>"

if __name__=="__main__":
    app.run(debug=False)