from flask import Flask, render_template, jsonify, request
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

@app.route('/wordcloud', methods=['GET', 'POST'])
def wordcloud():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('wordcloud.html')

@app.route('/toplist', methods=['GET', 'POST'])
def toplist():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('toplist.html')


if __name__ == "__main__":
  app.run(debug=True, port=3000)
