from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)

#This is an early version of the backend powering glitterskill

@app.route("/")
def index():
  data = ["Javascript", "Meteor", "Python", "Ruby On Rails", "Java"];
  return render_template('index.html', data=data)

def query_db(query, args=(), one=False):
  print 'running query'
  db = sqlite3.connect('database.db')
  cur = db.cursor()
  cur.execute(query, args)
  r = [dict((cur.description[i][0], value) \
             for i, value in enumerate(row)) for row in cur.fetchall()]
  cur.connection.close()
  db.close()
  return (r[0] if r else None) if one else r

@app.route('/rihanna')
def rihanna():
  return render_template('barebones.html')

@app.route('/wordcloud')
def wordcloud():
  return render_template('wordcloud.html')

@app.route('/toplist')
def toplist():
  return render_template('toplist.html')


if __name__ == "__main__":
  app.run(debug=True, port=4000)
