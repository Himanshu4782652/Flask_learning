from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check_palindrome", methods=["POST"])
def check_palindrome():
    name = request.form["name"].upper()
    reversed_name = name[::-1]

    if name == reversed_name:
        result = "Yes, the name is a palindrome!"
    else:
        result = "No, the name is not a palindrome."

    return render_template("result.html", name=name, result=result)


if __name__ == "__main__":
    app.run(debug=True)
