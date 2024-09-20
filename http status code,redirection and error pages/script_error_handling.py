from flask import Flask, request, redirect, url_for
from flask.templating import render_template

app = Flask(__name__)


@app.errorhandler(404)
def errorHandler(error):
    return render_template("404.html", context={'error':error}), 404


@app.route("/login")
def login():
    return """<p><form>
<input name="username"><br/>
<input type="submit">
</form></p>
"""


if __name__ == "__main__":
    app.run(debug=True)
