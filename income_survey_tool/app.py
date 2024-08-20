from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['income_survey']
collection = db['users']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_data = {
        'age': request.form['age'],
        'gender': request.form['gender'],
        'total_income': request.form['total_income'],
        'expenses': {
            'utilities': request.form.get('utilities'),
            'entertainment': request.form.get('entertainment'),
            'school_fees': request.form.get('school_fees'),
            'shopping': request.form.get('shopping'),
            'healthcare': request.form.get('healthcare')
        }
    }
    collection.insert_one(user_data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
