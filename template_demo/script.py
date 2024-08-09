from flask import Flask, render_template

app=Flask("__main__")

# @app.route("/printTable/<int:number>")
# def printTable(number):
#    return render_template("table.html",num=number)

@app.route("/staticDemo")
def static_demo():
    return render_template("static_demo.html")

if __name__=="__main__":
   app.run(debug=True)