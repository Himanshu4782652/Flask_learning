from flask import Flask,request

app=Flask(__name__)

@app.route("/requestDemo")

def request_demo():
   print(request.method)
   # print(request.__dict__.items())
   return "This page is designed to print's request object"

if __name__=="__main__":
   app.run(debug=True)