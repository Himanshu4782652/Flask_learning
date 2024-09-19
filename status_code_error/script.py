from flask import Flask
from flask import render_template, request, abort
from http import HTTPStatus

app = Flask(__name__)

@app.route('/printStatus')
def print_status():
 print(list(HTTPStatus))
 username=request.args.get('uname')
 if username == 'admin':
    return render_template('print_status.html', status=list(HTTPStatus))
 else:
    abort(403)

if __name__ == "__main__":
    app.run(debug=True)
