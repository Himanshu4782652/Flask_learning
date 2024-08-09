from flask import Flask

app = Flask(__name__)  # here we created object of flask

@app.route('/hello')  # create route for calling a function with the help of decorator

def helloWorld():      # here we created function of flask
   msg = "Hello Guest!!! Welcome to the world of programming."
   return msg

# below code is not necessary to run via flask run command which is 2nd way of running server
if __name__ == '__main__':
   app.run(debug=True)