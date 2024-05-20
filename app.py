from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('greet_user', name=name))
    return render_template('greet.html')

@app.route('/greet/<name>')
def greet_user(name):
    return render_template('greet_user.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
