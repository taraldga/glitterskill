from flask import Flask
app = Flask(__name__)

#This is an early version of the backend powering glitterskill

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
