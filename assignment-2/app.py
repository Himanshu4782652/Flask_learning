from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/sorting", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_list = request.form.get("input_list")
        input_list = list(map(int, input_list.split(",")))
        sorted_list = sorted(input_list)
        first_element = sorted_list[0]
        last_element = sorted_list[-1]
        return render_template(
            "index.html",
            sorted_list=sorted_list,
            first_element=first_element,
            last_element=last_element,
        )
    return render_template("index.html") 
if __name__ =="__main__":
   app.run(debug=True)
