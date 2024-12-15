from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')

#app.add_template_filter(today, 'today')

@app.add_template_global
def repeat (s, n):
    return s * n

#app.add_template_global(repeat, 'repeat')

from datetime import datetime

@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('hello', name = 'Jose', age = 18))
    print(url_for('code', code = 'print("hola")'))
    name = 'Jose'
    friends = ['alexander', 'roel', 'juan', 'pedro']
    date = datetime.now()
    return render_template(
        'index.html',
        name=name,
        friends=friends,
        date=date,
        )

@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
@app.route('/hello/<name>/<int:age>/<email>')
def hello(name = None, age = None, email = None):
    my_data = {
        'name': name,
        'age': age,
        'email': email
    }
    return render_template('hello.html', data=my_data)

from markupsafe import escape
@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'