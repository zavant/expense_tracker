from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expenses = db.Column(db.String(300), nullable=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, expenses, name, location):
        self.expenses = expenses
        self.name = name
        self.location = location


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/')
def index():
    all_data = Tracker.query.all()
    return render_template('main.html', trackers=all_data)


@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'POST':
        expenses = request.form['expenses']
        name = request.form['name']
        location = request.form['location']

        my_data = Tracker(expenses, name, location)
        db.session.add(my_data)
        db.session.commit()

        flash("Expense Successfully Added")
        return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Tracker.query.get(request.form.get('id'))

        my_data.expenses = request.form['expenses']
        my_data.name = request.form['name']
        my_data.location = request.form['location']

        db.session.commit()
        flash("Records Sucessfully Updated")
        return redirect(url_for('index'))


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Tracker.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Expense Deleted")

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
