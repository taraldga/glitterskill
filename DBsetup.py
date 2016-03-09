import sqlite3

DATABASE = 'database.db'

conn = sqlite3.connect(DATABASE)
c = conn.cursor()
query = """CREATE TABLE Job (
            id integer
            firm text,
            city text,
            postcode integer,
            deadline text,
            title text,
            branch text,
            source text,
            description text
          )"""
c.execute(query);
