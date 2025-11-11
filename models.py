from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)                # e.g. "Australia"
    continent = db.Column(db.String(50))                            # e.g. "Oceania"
    capital_city = db.Column(db.String(100), nullable=False)        # e.g. "Canberra"
    population = db.Column(db.Integer, nullable=False)              # e.g. 25600000
    language = db.Column(db.String(50))                             # e.g. "English"
    currency = db.Column(db.String(50))                             # e.g. "Australian Dollar"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)    # timestamp for record creation
    map = db.Column(db.String())                                    # country map
    flag = db.Column(db.String())                                   # country flag


    def __repr__(self):
        return f'<Task {self.title}>'
    
@app.route('/add')
def add_country():
    pass