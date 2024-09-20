from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

tasks = []

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
            tasks.append({'task':task, 'added by': session['username']})
    return render_template('todo.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)