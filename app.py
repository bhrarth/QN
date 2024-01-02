from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Replace 'username', 'password', 'cluster_name', and 'phonenumbers' with your actual MongoDB connection details
mongo_client = MongoClient('mongodb+srv://bharath:arK5nNpCkKMwLXS4@cluster0.a0zbdsq.mongodb.net/test')
db = mongo_client['phonenumbers']
collection = db['phonenumbers']

class PhoneNumber:
    def __init__(self, number):
        self.number = number

# Check if the collection exists, create it if not
if 'phonenumbers' not in db.list_collection_names():
    db.create_collection('phonenumbers')
    print("Collection created successfully")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        number = request.form['number']

        # Validate and store the number in the MongoDB collection
        if number:
            try:
                new_number = PhoneNumber(number=number)
                collection.insert_one(new_number.__dict__)
                print("Submit successful")

            except Exception as e:
                print(f"Error: {e}")
                return f"Error: {e}"

    return render_template('success.html') 

if __name__ == '__main__':
    app.run(debug=True)
