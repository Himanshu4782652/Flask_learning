from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("mycollege.db")
cur = conn.cursor()
cur.execute("select count(*) from sqlite_master where type='table' and name='student'")
if cur.fetchone()[0] == 1:
    print("Table Already exists")
else:
    conn.execute("CREATE TABLE student(name TEXT,addr TEXT,city TEXT,pin TEXT)")
    print("Table created successfully")
conn.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/deleteInput")
def delete_input():
    return render_template("delete_input.html")


@app.route("/deleteStudent", methods=["POST"])
def delete_student():
    stud_name = request.form.get("txtname")
    try:
        with sqlite3.connect("mycollege.db") as conn:
            my_query = "delete from student where name='" + stud_name + "';"
            conn.execute(my_query)
            conn.commit()
            msg = "total rows deleted are:" + str(conn.total_changes)
    except:
        conn.rollback()
        msg = "Sorry...Could not delete any records"
    finally:
        conn.close()
    return render_template("success.html", msg=msg)


@app.route("/addStudent")
def add_student():
    return render_template("add_student.html")


@app.route("/saveStudent", methods=["GET", "POST"])
def save_student():
    msg = ""
    if request.method == "POST":
        try:
            name = request.form.get("studname")
            addr = request.form.get("studaddr")
            city = request.form.get("studcity")
            pin = request.form.get("studpin")

            with sqlite3.connect("mycollege.db") as conn:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO student(name, addr, city, pin) values(?, ?, ?, ?)",
                    (name, addr, city, pin),
                )
                conn.commit()
                msg = "data inserted successfully"

        except:
            conn.rollback()
            msg = "Could not Insert data into student"
    return render_template("success.html", msg=msg)


@app.route("/listStudent")
def list_student():
    conn = sqlite3.connect("mycollege.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("select * from student")
    row = cur.fetchall()

    return render_template("view.html", row=row)


if __name__ == "__main__":
    app.run(debug=True)
