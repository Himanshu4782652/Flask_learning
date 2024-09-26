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


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
