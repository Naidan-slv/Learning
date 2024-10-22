from app import db

class Person(db.Model):
    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key=True)
    # the pid is the the primary key and the db.integer is the data type
    name = db.Column(db.Text, nullable=False)
    # it is not allowed to be empty hence the nullable=False
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __repr__(self):
        return f"Person {self.name} is {self.age} years old and works as a {self.job}"