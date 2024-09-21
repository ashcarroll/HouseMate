from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'a_secret_lock'

tasks = []
completed_tasks = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/set_name', methods=['POST'])
def set_name():
    session ['username'] = request.form['name']
    return redirect(url_for('todo'))

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form['task']
        if task.strip():
            tasks.append({'task':task, 'added_by': session['username']})
    return render_template('todo.html', tasks=tasks)

@app.route('/complete_task/<int:task_index>', methods=['POST'])
def complete_task(task_index):
    completed_task = tasks.pop(task_index)
    completed_task['completed_by'] = session ['username']
    completed_tasks.append(completed_task)
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)