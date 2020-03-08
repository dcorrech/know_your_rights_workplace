#!flask/bin/python
from flask import Flask, jsonify, abort, request
from to_csv import get_value
from get_similar_text import get_most_similar_text
import csv
from flask_cors import CORS, cross_origin

# add call to to_csv function to load csv
values = get_value()

#set unique userid for input to get_most_similar_text
x=1

# send csv to similarity function, return most similar post in csv
get_most_similar_text('kyr_data.csv', x)
result = []
with open('results.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        result.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
        id = row[0]
        what_happened = row[1]
        employer = row[2]
        reason = row[3]
        province = row[4]
        details = row[5]
        resolution = row[6]


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# cors = CORS(app, resources={r"/task": {"origins": "http://localhost:5000"}})

tasks = [
    {
        'id': id,
        'what_happened': what_happened,
        'employer': employer,
        'reason': reason,
        'province': province,
        'details': details,
        'resolution': resolution,
    }
]

@app.route('/tasks', methods = ['GET'])
@cross_origin()
def get_tasks():
    return jsonify( {'tasks': tasks})

@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True)