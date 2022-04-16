from app import app
from app import db
from app.models import Roles, Parent, Child
import sys


db.drop_all()
db.create_all()

role1 = Roles(id=1, description='Student')
role2 = Roles(id=2, description='Business')
role3 = Roles(id=3, description='Administrator')
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
db.session.commit()