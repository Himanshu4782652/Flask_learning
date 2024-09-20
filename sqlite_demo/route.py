from flask import Flask
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("mycollege.db")
cur=conn.cursor()
cur.execute("select count(*) from sqlite_master where type='table' and name='student'")
if cur.fetchone()[0]==1:
 print("Table Already exists")
else:
    conn.execute("CREATE TABLE student(name TEXT,addr TEXT,city TEXT,pin TEXT)")
    print("Table created successfully")
conn.close()

if __name__ == "__main__":
    app.run(debug=True)
