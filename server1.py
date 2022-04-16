# server micro kelompok
from flask import Flask, jsonify, make_response
import pymysql
import json

app = Flask(__name__)


mydb = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="northwind"
)


@app.route('/', methods=['GET'])
def get_data_siswa():
    query = "SELECT * FROM customers"
    values = ()
    mycursor = mydb.cursor()
    mycursor.execute(query, values)
    row_headers = [x[0] for x in mycursor.description]
    data = mycursor.fetchall()
    json_data = []
    for result in data:
        json_data.append(dict(zip(row_headers, result)))
    return make_response(jsonify(json_data), 200)


app.run(host='0.0.0.0', port=8091)
