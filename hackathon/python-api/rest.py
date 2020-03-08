#!flask/bin/python
from flask import Flask, jsonify, abort, request
from to_csv import get_value
from get_similar_text import get_most_similar_text
import csv

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


app = Flask(__name__)

tasks = [
    {
        'id': values[x][0],
        'what_happened': values[x][1],
        'employer': values[x][2],
        'reason': values[x][3],
        'province': values[x][4],
        'details': values[x][5],
        'resolution': values[x][6],
    }
]

@app.route('/tasks', methods = ['GET'])
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