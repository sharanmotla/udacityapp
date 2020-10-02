from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sharanmotla@localhost:5000/sharanmotla'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Person(db.Model):
__tablename__ = 'persons'
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(), nullable=False)

@app.route('/')
def index():
return 'Hello World' 