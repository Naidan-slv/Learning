from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, CHAR
from sqlalchemy.ext.declarative import declarative_base

# essentially the base class which we will extend. What we inherit from
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "persons"
    #next we define the columns which are essentially our attibutes

    ssn = Column("ssn",Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", String)
    age = Column("age", Integer)


    # provide the attribute name inside python then you say its a column and then we speficy
    #  the database name and then you specify the database datatype and set some optional paramaters

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        # a function that allows us to specify how we want to print a person object
        return f"({self.ssn} {self.firstname} {self.lastname}({self.gender},{self.age})"
    
class Thing(Base):
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column("owner", Integer, ForeignKey("persons.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):
        return f"({self.tid} {self.description} {self.owner})"

engine = create_engine("sqlite:///mydb2.db", echo=True)
Base.metadata.create_all(bind=engine)
# takkes all the classes that extends from base and creates them in the database.

Session = sessionmaker(bind=engine)
session = Session()
# session is the instance and Session() is the class 

person = Person(12312,"mike","smith", "m", 35)
session.add(person)
session.commit()

p1 = Person(123123,"angel","deee", "m", 35)
p2 = Person(123222,"bob","smith", "m", 35)
p3 = Person(123333,"yalah","smith", "f", 20)

session.add(p1)
session.add(p2)
session.add(p3)

session.commit()

results = session.query(Person).all()
print(results)

t1 = Thing(1, "a thing", p1)
session.add(t1)
session.commit()