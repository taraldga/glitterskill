from flask import Flask, render_template
from flask import render_template
app = Flask(__name__)

#This is an early version of the backend powering glitterskill

@app.route("/")
def index():
  return render_template('index.html')

if __name__ == "__main__":
  app.run()
