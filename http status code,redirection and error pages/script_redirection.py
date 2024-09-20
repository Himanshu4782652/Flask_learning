from flask import Flask, request, redirect, url_for
from flask.templating import render_template

app = Flask(__name__)


@app.route("/redirectedPage")
def redirected_page():
    print("Request arguments again from redirectedPage: ", request.args)
    # return "This is redirected Page"
    return redirect('http://www.google.com')


@app.route("/redirectedDemo")
def redirect_demo():
    print("Request arguments from demo: ", request.args)
    res=redirected_page()
    return res


if __name__ == "__main__":
    app.run(debug=True)
