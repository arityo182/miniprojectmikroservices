from flask import Flask
import flask
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/server1/getdata', methods=['GET'])
def get_data():
    url = 'http://119.13.124.218:8091/'
    response = requests.request('GET', url)
    return response.text


@app.route('/server2/getdata', methods=['GET'])
def get_data2():
    url = 'http://119.13.124.218:8092'
    response = requests.request('GET', url)
    return response.text


if __name__ == '__main__':
    app.run(debug=True, port=8090, host="0.0.0.0")
