from app import app
from app import db
#from sqlalchemy.orm import backref, relationship
#from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey, String, Text, Date, Boolean
#from sqlalchemy.ext.declarative import declarative_base
from app.models import Roles
import sys


""" db.drop_all()
db.create_all()

role1 = Roles(description='Student')
role2 = Roles(description='Business')
role3 = Roles(description='Administrator')
db.session.add(role1)
db.session.add(role2)
db.session.add(role3)

parent1 = Parent()
child1 = Child(parent_id=1)
child2 = Child(parent_id=1)

parent2 = Parent()
child3 = Child(parent_id=2)
child4 = Child(parent_id=2)

db.session.add(parent1)
db.session.add(child1)
db.session.add(child2)

db.session.add(parent2)
db.session.add(child3)
db.session.add(child4)
db.session.commit() """

""" if __name__ == "__main__":
    create_app().run() """