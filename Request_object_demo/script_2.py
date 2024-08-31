from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def take_data():
    return render_template("take_data_2.html")


@app.route("/fetchData", methods=["post"])
def fetch_data():
    # print(request.form)
    # return "Request form is printed"
    return "<h2>The language is {} and the framework is {}".format(
        request.form.get("txtlanguage"), request.form.get("txtframework")
    )


if __name__ == "__main__":
    app.run(debug=True)
