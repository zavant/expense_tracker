from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expenses = db.Column(db.String(300), nullable=False)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        expense_content = request.form['expenses']
        new_expense = Tracker(expenses=expense_content)
        
        try:
            db.session.add(new_expense)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Tracker.query.order_by(Tracker.date_created).all()
        return render_template('main.html', tasks = tasks )

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Tracker.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error deleting task'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Tracker.query.get_or_404(id)
    if request.method == 'POST':
        task.expenses = request.form['expenses']

        try: 
            db.session.commit()
            return redirect('/')
        except: 
            return 'Error updating'
    else:
        return render_template('update.html', task=task)



if __name__ == '__main__':
    app.run(debug=True)