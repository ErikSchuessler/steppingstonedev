from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
#from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from wtforms_alchemy import ModelForm, ModelFieldList
from wtforms.fields import FormField

class Parent(db.Model):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)

class Child(db.Model):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", backref=backref("child", uselist=False))

# Define the DB schema
class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64), unique=True, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return self.city + ': ' + str(self.population)

class User(UserMixin, db.Model):
    __tablename__='Users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64), unique=False, nullable=False)
    lastName = db.Column(db.String(64), unique=False, nullable=False)
    businessName = db.Column(db.String(64), unique=False, nullable=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('Roles.id'), nullable=False)
    
    
    profile = db.relationship('Profile', backref='User', lazy=True, uselist=False)



    def set_password(self, passwordToEncrypt):
        self.password = generate_password_hash(passwordToEncrypt)
    
    def check_password(self, passwordToCheck):
        return check_password_hash(self.password, passwordToCheck)
    
    def __repr__(self):
        return f"{self.firstName}, {self.lastName}, {self.email}, {self.password}, {self.role}"

class Profile(db.Model):
    __tablename__='Profiles'
    id = db.Column(db.Integer, primary_key=True)


    userId = db.Column(db.Integer, db.ForeignKey('Users.id'))
    #user = relationship("User", backref=backref('Profile', uselist=False))


    phoneNumber = db.Column(db.String(64), nullable=True)
    contactEmail = db.Column(db.String(64), unique=False, nullable=True)
    highSchool = db.Column(db.String(150), unique=False, nullable=True)
    university = db.Column(db.String(150), unique=False, nullable=True) 
    introduction = db.Column(db.Text, nullable=True)

   
    def __repr__(self):
        return f"{self.id}"

class Roles(db.Model):
    __tablename__='Roles'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64), unique=False, nullable=False)
    
    def __repr__(self):
        return f"{self.id}, {self.description}, {self.role}"

class JobHistory(db.Model):
    __tablename__='JobHistories'
    id = db.Column(db.Integer, primary_key=True)
    profileId = db.Column(db.Integer, ForeignKey('Profiles.id'), nullable=False)
    title = db.Column(db.String(150), unique=False, nullable=True)
    companyName = db.Column(db.String(150), unique=False, nullable=True)
    startDate = db.Column(db.Date, unique=False, nullable=True)
    endDate = db.Column(db.Date, unique=False, nullable=True)
    description = db.Column(db.Text, unique=False, nullable=True)

class Reference(db.Model):
    __tablename__='References'
    id = db.Column(db.Integer, primary_key=True)
    profileId = db.Column(db.Integer, ForeignKey('Profiles.id'), nullable=False)
    name = db.Column(db.String(150), unique=False, nullable=True)
    email = db.Column(db.String(150), unique=False, nullable=True)
    phoneNumber = db.Column(db.String(150), unique=False, nullable=True)
    organization = db.Column(db.String(150), unique=False, nullable=True)

class Listing(db.Model):
    __tablename__='Listings'
    id = db.Column(db.Integer, primary_key=True)
    businessId = db.Column(db.Integer, ForeignKey('Users.id'), nullable=False)
    streetAddress = db.Column(db.String(150), unique=False, nullable=False)
    city = db.Column(db.String(150), unique=False, nullable=False)
    state = db.Column(db.String(150), unique=False, nullable=False)
    zip = db.Column(db.String(10), unique=False, nullable=False)

    positionTitle = db.Column(db.String(150), unique=False, nullable=False)
    qualifications = db.Column(db.Text, nullable=False) 
    isInternship = db.Column(db.Boolean, nullable=False)
    isPartTime = db.Column(db.Boolean, nullable=False)
    description = db.Column(db.Text, nullable=False)
    benefits = db.Column(db.Text, nullable=False)
    salary = db.Column(db.String(150), unique=False, nullable=False)
    
    def __repr__(self):
        return f"{self.id}, {self.businessId}"

class Application(db.Model):
    __tablename__='Applications'
    id = db.Column(db.Integer, primary_key=True)
    profileId = db.Column(db.Integer, ForeignKey('Profiles.id'), nullable=False)
    listingId = db.Column(db.Integer, ForeignKey('Listings.id'), nullable=False)
    def __repr__(self):
        return f"{self.id}, {self.profileId}, {self.listingId}"

@login.user_loader
def load_user(id):
    return db.session.query(User).get(int(id))






