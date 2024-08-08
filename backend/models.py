from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(2000), nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f"About('{self.text}', '{self.last_updated}')"
    


