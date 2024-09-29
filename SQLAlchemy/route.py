from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mycollege.db"

db = SQLAlchemy(app)


class student(db.Model):
    id = db.Column("student_id", db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    addr = db.Column(db.String(100))
    city = db.Column(db.String(50))
    pin = db.Column(db.String(10))

    def __init__(self, name, addr, city, pin) -> None:
        super().__init__()
        self.name = name
        self.addr = addr
        self.city = city
        self.pin = pin


@app.route("/insert")
def insert_student():
    return render_template("insert_student.html")


@app.route("/queryStudent")
def queryStudent():
 all_student = student.query.all()
 return render_template("/listStudent.html", data=all_student)

@app.route("/submitStudent", methods=["POST"])
def submit_student():
    name = request.form.get("txtname")
    address = request.form.get("txtaddr")
    city = request.form.get("txtcity")
    pin = request.form.get("txtpin")
    stud = student(name, address, city, pin)

    db.session.add(stud)
    db.session.commit()
    msg = "Record Inseted Successfully"
    return render_template("success.html", msg=msg)


if __name__ == "__main__":
    with app.app_context():  # Push application context
        db.create_all()  # Create tables in the database
    app.run(debug=True)
