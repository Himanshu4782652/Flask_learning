from flask import Flask, render_template

app = Flask("__main__")

# @app.route("/base")
# def base():
#    return render_template("base.html")

# @app.route("/home")
# def home():
#    return render_template("home.html")

# @app.route("/about")
# def about():
#    return render_template("about.html")

# @app.route("/product")
# def product():
#    return render_template("product.html")


@app.route("/filterDemo")
def filter_demo():
    names = ["sita", "gita", "mita", "tina", "nita"]
    numbers = [21, 23, 26, 22, 28]
    return render_template(
        "filter_demo.html", context={"names": names, "numbers": numbers}
    )


@app.route("/varDemo")
def var_demo():
    username = "Himanshu"
    password = "secret3"
    return render_template(
        "var_demo.html", context={"username": username, "password": password}
    )


if __name__ == "__main__":
    app.run(debug=True)
