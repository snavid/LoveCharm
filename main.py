from flask import Flask, render_template, session, flash
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from LoveCalculator import NormalLoveCalc, BestLoveCalc
from os import environ


app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/statics')
api = Api(app)
app.config['SECRET_KEY'] = 'i love you'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        

class LoveCalculator(Resource):
    def get(self, name1, name2):
       
        Normalpercentage = NormalLoveCalc(name1, name2)
        reversedNormalpercentage = NormalLoveCalc(name2, name1)
        Truepercentage = BestLoveCalc(name1, name2)
        
        
        return int(Normalpercentage.split('%')[0])


   
api.add_resource(LoveCalculator, '/api/<string:name1>/<string:name2>')

with app.app_context():
    db.create_all()
    
@app.route('/', methods=['GET', 'POST'])
def homepage():
    session['data'] = {}
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
        
    