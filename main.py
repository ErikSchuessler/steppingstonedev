from app import app
from app import db
from app.models import Roles
import sys


#db.drop_all()

"""
db.create_all()

role1 = Roles(description='Student')
role2 = Roles(description='Business')
role3 = Roles(description='Administrator')
db.session.add(role1)
db.session.add(role2)
db.session.add(role3)
"""


#use this and 'python3 main.py' at terminal to troubleshoot import errors
#if __name__ == "__main__":
#create_app().run()