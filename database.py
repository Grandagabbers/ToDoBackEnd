from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'task': 'kamer schoonmaken',
        'done': False
    },
    {
        'id': 2,
        'task': 'kamer opruimen',
        'done': False
    },
    {
        'id': 3,
        'task': 'kamer inrichten',
        'done': False
    }
]


@app.route('/todos')
def get_task():
    return jsonify(tasks)


@app.route('/todos/change', methods=['PUT'])
def change_task():
    data = request.get_json()
    id = data["id"]
    for x in tasks:
        if id == x["id"]:
            print("test")
            x["done"] = data["done"]
            x["task"] = data["task"]
    return data


@app.route('/todos/post', methods=['POST'])
def post_task():
    data = request.get_json()
    print(data)
    return data


@app.route('/todos/delete', methods=['DELETE'])
def delete_task():
    data = request.get_json()
    print(data)
    return ''


@app.route('/todos/update', methods=['PUT'])
def update_task():
    data = request.get_json()
    id = data["id"]
    for x in tasks:
        if id == x["id"]:
            print(id)
            x["done"] = data["done"]
            x["task"] = data["task"]
    print(id)
    return data


@app.route('/todos/realUpdate', methods=['UPDATE'])
def realUpdate_task():
    return''


if __name__ == '__main__':
    app.run(debug=True)


