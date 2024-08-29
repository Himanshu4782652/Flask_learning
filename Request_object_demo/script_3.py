from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route("/makeJson")
def make_json():
    person = {
        "name": "Himanshu",
        "language": "python",
        "framework": ["flask", "django", "bottle"],
    }
    res = requests.post("http://127.0.0.1:5000/processJson", json=person)
    return res.text


@app.route("/processJson", methods=["post"])
def process_json():
    if request.is_json:
        #   return "It has json data"
        return request.json
    else:
        return "It does'nt have json data"


if __name__ == "__main__":
    app.run(debug=True)
