from app import app
from app import db
from app.models import Roles
import sys


#db.drop_all()
#db.create_all()

""" role1 = Roles(id=1, description='Student')
role2 = Roles(id=2, description='Business')
role3 = Roles(id=3, description='Administrator')
db.session.add(role1)
db.session.add(role2)
db.session.add(role3)
db.session.commit() """