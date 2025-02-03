from app import db

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable= False)
    description = db.Column(db.Text,nullable=False)

    def __repr__(self):
        return f'<Dog {self.name}>'