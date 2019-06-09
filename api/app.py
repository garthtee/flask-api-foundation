import json
from flask import Flask
from .utils import json_response

app = Flask(__name__)

test_object = [{
    'id': 1,
    'title': 'A Title'
}]

@app.route('/')
def index():
    return json_response(json.dumps(test_object))

@app.errorhandler(404)
def not_found(error):
    return json_response(status=404)

@app.errorhandler(500)
def not_found(error):
    return json_response(status=500)
