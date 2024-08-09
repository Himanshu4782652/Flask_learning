from flask import Flask
from flask import url_for

app = Flask("__main__")


@app.route("/")
def index():
    return "This is index"


# 1st method of routing
@app.route("/home")
@app.route("/home/<username>")
def home(username="Guest"):
    return "Welcome to Home page of " + username


# 2nd method
def blog():
    msg = "These are blogs"
    return msg


app.add_url_rule("/get_blogs", "blog", blog)  # 2nd method of routing


@app.route("/blog/<int:blog_no>")
def get_blog(blog_no):
    return "This is blog number: " + str(blog_no)


@app.route("/check_odd_even/<int:number>")
def check_odd_even(number):
    if number % 2 == 0:
        return "Number is <b> Even </b>"
    return "Number is <b> Odd </b>"


with app.test_request_context():
    print(url_for("index"))
    print(url_for("home", username="Rupal Shah"))
    print(url_for("home", username="Rupal Shah", password="Top Secret"))


app.add_url_rule("/get_blog", "blog", blog)
if __name__ == "__main__":
    app.run(debug=True)
