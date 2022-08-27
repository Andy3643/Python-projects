from app import db
 
class City(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.sring(50), nullable=False)