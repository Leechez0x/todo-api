from flask import Flask, jsonify, request

app = Flask(__name__)

tasks =[
    {'id':1, 'title': 'Learn Flask', 'done': False},
    {'id':2, 'title': 'Build an API', 'done': False},
    {'id':3, 'title': 'Push to GitHub', 'done': True}
]

@app.route('/api/tasks')
def get_tasks():
    return jsonify(tasks)


@app.route('/api/tasks/<int:task_id>')
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods =['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({'message': 'Task deleted'})
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)