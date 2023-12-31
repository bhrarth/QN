from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Replace 'postgres', 'Bharath@postsql7', and 'qa_database' with your actual PostgreSQL credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin711@localhost/phonenumbers'
db = SQLAlchemy(app)

class PhoneNumber(db.Model):
    __tablename__='phonenumbers'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(15), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        number = request.form['number']

        # Validate and store the number in the database
        if number:
            try:
                new_number = PhoneNumber(number=number)
                db.session.add(new_number)
                db.session.commit()
                print("Submit successful")
                
            except Exception as e:
                db.session.rollback()
                print(f"Error: {e}")
                return f"Error: {e}"

    return render_template('success.html') 

    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created successfully")
    app.run(debug=True)
