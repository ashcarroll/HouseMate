from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/set_name', methods=['POST'])
def set_name():
    session ['username'] = request.form['name']
    return redirect(url_for'todo')

if __name__ == '__main__':
    app.run(debug=True)