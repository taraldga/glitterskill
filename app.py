from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

#This is an early version of the backend powering glitterskill

@app.route("/")
def index():
  data = ["Javascript", "Meteor", "Python", "Ruby On Rails", "Java"];
  return render_template('barebones.html', data=data)

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

if __name__ == "__main__":
  app.run(debug=True)
