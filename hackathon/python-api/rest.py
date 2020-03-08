#!flask/bin/python
from flask import Flask, jsonify, abort, request

from to_csv import get_value
# add call to to_csv functions to load csv


# send csv to similarity function, return most similar post
#### ADD SIMILARITY CALL HERE ####

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': get_value(), 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
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