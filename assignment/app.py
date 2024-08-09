from flask import Flask, jsonify
from datetime import datetime

app=Flask(__name__)

def get_greetings():
   currentTime=datetime.now().time()
   if currentTime < datetime.strptime("12:00","%H:%M").time():
      return "Good Morning"
   elif currentTime < datetime.strftime("16:00","%H:%M").time():
      return "Good Afternoon"
   elif currentTime < datetime.strftime("21:00","%H:%M").time():
      return "Good Evening"
   else:
      return "Good Night"
   
@app.route("/")
def greet():
   greeting=get_greetings()
   return jsonify({"message": greeting})

if __name__=="__main__":
   app.run(debug=True)