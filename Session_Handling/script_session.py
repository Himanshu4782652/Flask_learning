from flask import Flask, session, request,render_template

app = Flask(__name__)

@app.route("/login", methods=["POST","GET"])
def login():
   if request.method=="POST":
      uname=session['username']
      return render_template("/get_profile.html")

if __name__ == "__main__":
    app.run(debug=True)
