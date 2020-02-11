from app import db

class Drink(db.Model):
    __tablename__='drinks'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime())
    btype = db.Column(db.String())
    name = db.Column(db.String())
    price = db.Column(db.Numeric())
    desiltr = db.Column(db.Numeric())
    permille = db.Column(db.Numeric())
    place = db.Column(db.String())
    month = db.Column(db.Integer())
    year = db.Column(db.Integer())

    def __init__(self, date, btype, name, place):
        self.date = date
        self.btype = btype 
        self.name = name
        self.place = place

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'date' : self.date,
            'btype': self.btype,
            'name': self.name,
            'price': self.price,
            'desiltr': self.desiltr,
            'permille': self.permille,
            'place': self.place,
            'month': self.month,
            'year': self.year
        }