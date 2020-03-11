import flask

from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/report', methods=['GET'])
def report():
    args = request.args
    if 'date' in args:
        print(args['date'])
    return "<h1>Hello world</p>"

app.run()