from app import db
from sqlalchemy import Column, ForeignKey, Integer, String
#from sqlalchemy.orm import declarative_base
#from sqlalchemy.orm import relationship
from wtforms_alchemy import ModelForm, ModelFieldList
from wtforms.fields import FormField


# Define the DB schema
class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64), unique=True, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return self.city + ': ' + str(self.population)

class User(db.Model):
    __tablename__='Users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64), unique=False, nullable=False)
    lastName = db.Column(db.String(64), unique=False, nullable=False)
    businessName = db.Column(db.String(64), unique=False, nullable=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), unique=False, nullable=False)
    role = db.Column(db.Integer, ForeignKey('Roles.id'), nullable=False)
    
    def __repr__(self):
        return f"{self.firstName}, {self.lastName}, {self.email}, {self.password}, {self.role}"

class Roles(db.Model):
    __tablename__='Roles'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64), unique=False, nullable=False)
    
    def __repr__(self):
        return f"{self.id}, {self.description}, {self.role}"

class Profile(db.Model):
    __tablename__='Profiles'
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.Integer, ForeignKey('Users.id'), nullable=False)
    phoneNumber = db.Column(db.String(64), nullable=True)
    contactEmail = db.Column(db.String(64), unique=False, nullable=True)
    highSchool = db.Column(db.String(150), unique=False, nullable=True)
    university = db.Column(db.String(150), unique=False, nullable=True) 
    introduction = db.Column(db.Text, nullable=True)

   
    def __repr__(self):
        return f"{self.id}, {self.studentId}"

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







