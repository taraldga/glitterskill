from flask import Flask, render_template, jsonify
app = Flask(__name__)

#This is an early version of the backend powering glitterskill

@app.route("/")
def index():
  return render_template('index.html')


@app.route("/data")
def data():
  data = {
    "job" : {
      "id": 123452,
      "title": "Software Developer",
      "firm": "Bekk Consulting",
      "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit natus quo facere reprehenderit ullam ratione, beatae, repudiandae iure totam exercitationem nihil voluptas neque, illo aliquam quasi distinctio fuga consequuntur saepe!",
      "type": "partime",
      "industry": "IT",
      "location": "Russia",
      "contact": "martin@finn.no",
      "deadline": "01.03.16",
      "date": "01.06.16",
      "background": "engineer"
    }
  }
  return jsonify(data)


if __name__ == "__main__":
  app.run(debug=True)
