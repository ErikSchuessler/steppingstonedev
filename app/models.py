from app import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

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
    studentPhoneNum = db.Column(db.String, nullable=True)
    studentContactEmail = db.Column(db.String(64), unique=False, nullable=True)
    studentHighSchool = db.Column(db.String(150), unique=False, nullable=True)
    studentUni = db.Column(db.String(150), unique=False, nullable=True) 

    introduction = db.Column(db.Text, nullable=True)

    jobOneName = db.Column(db.String(150), unique=False, nullable=True)
    jobOneDescrip = db.Column(db.Text, nullable=True)

    jobTwoName = db.Column(db.String(150), unique=False, nullable=True)
    jobTwoDescrip = db.Column(db.Text, nullable=True)

    jobThreeName = db.Column(db.String(150), unique=False, nullable=True)
    jobThreeDescrip = db.Column(db.Text, nullable=True)

    referenceOne = db.Column(db.Text, nullable=True)
    referenceTwo = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"{self.id}, {self.studentId}"

class Listing(db.Model):
    __tablename__='Listings'
    id = db.Column(db.Integer, primary_key=True)
    businessId = db.Column(db.Integer, ForeignKey('Users.id'), nullable=False)
    businessStreetAddress = db.Column(db.String(150), unique=False, nullable=False)
    businessCity = db.Column(db.String(150), unique=False, nullable=False)
    businessState = db.Column(db.String(150), unique=False, nullable=False)
    businessZip = db.Column(db.Integer, unique=False, nullable=False)

    positionName = db.Column(db.String(150), unique=False, nullable=False)
    positionQualifications = db.Column(db.Text, nullable=False) 
    isInternship = db.Column(db.Boolean, nullable=False)
    isPartTime = db.Column(db.Boolean, nullable=False)
    positionDescrip = db.Column(db.Text, nullable=False)
    positionBenefits = db.Column(db.Text, nullable=False)
    positionSalary = db.Column(db.String(150), unique=False, nullable=False)
    
    def __repr__(self):
        return f"{self.id}, {self.businessId}"

class Application(db.Model):
    __tablename__='Applications'
    id = db.Column(db.Integer, primary_key=True)
    profileId = db.Column(db.Integer, ForeignKey('Profiles.id'), nullable=False)
    listingId = db.Column(db.Integer, ForeignKey('Listings.id'), nullable=False)
    def __repr__(self):
        return f"{self.id}, {self.profileId}, {self.listingId}"







