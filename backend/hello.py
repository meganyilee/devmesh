from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/kanyeClassify', methods=['POST'])
def kanyeClassify():
    req_data = request.get_json()
    return req_data['stuff']
