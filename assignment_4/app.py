from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = "your_secret_key"


@app.route("/")
def index():
    # Check if a session exists
    if "visit_count" not in session:
        session["visit_count"] = 0

    # Increment the visit count
    session["visit_count"] += 1

    # Get the cookie value if it exists
    cookie_value = request.cookies.get("visit_count_cookie")
    if cookie_value:
        # Convert the cookie value to an integer
        cookie_value = int(cookie_value)
    else:
        cookie_value = 0

    # Increment the cookie value
    cookie_value += 1

    # Set a new cookie with the incremented value
    resp = make_response(
        render_template(
            "index.html", visit_count=session["visit_count"], cookie_value=cookie_value
        )
    )
    resp.set_cookie("visit_count_cookie", str(cookie_value))
    return resp


if __name__ == "__main__":
    app.run(debug=True)
