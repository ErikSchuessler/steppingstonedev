from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, SelectField, TextAreaField, RadioField, DateField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    city = StringField('City:', validators=[DataRequired()])
    population = IntegerField('Population: ', validators=[DataRequired()])
    submit = SubmitField('Save')

class DeleteForm(FlaskForm):
    city = StringField('City:', validators=[DataRequired()])
    submit = SubmitField('Delete')

class SearchForm(FlaskForm):
    city = StringField('City:', validators=[DataRequired()])
    submit = SubmitField('Search')

class PopulationFilterForm(FlaskForm):
    population = IntegerField('Minimum population: ', validators=[DataRequired()])
    submit = SubmitField('Search')

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class StudentRegistrationForm(FlaskForm):
    firstName = StringField('First name:', validators=[DataRequired()])
    lastName = StringField('Last name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Register')

class BusinessRegistrationForm(FlaskForm):
    firstName = StringField('First name:', validators=[DataRequired()])
    lastName = StringField('Last name:', validators=[DataRequired()])
    businessName = StringField('Business Name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    password = StringField('Password:', validators=[DataRequired()])
    submit = SubmitField('Register')

class ListingForm(FlaskForm):
    streetAddress = StringField('Street address: ', validators=[DataRequired()])
    city = StringField('City: ', validators=[DataRequired()])
    state = StringField('State: ', validators=[DataRequired()])
    zip = StringField('ZIP code: ', validators=[DataRequired()])
    positionTitle = StringField('Position title: ', validators=[DataRequired()])
    qualifications = TextAreaField('Qualifications: ', validators=[DataRequired()])
    isInternship = RadioField('Position type: ', choices = [(1, 'Internship'), (0, 'Job')], validators=[DataRequired()])
    isPartTime = RadioField('Work time: ', choices = [(1, 'Part-time'), (0, 'Full-time')], validators=[DataRequired()])
    description = TextAreaField('Describe the position...', validators=[DataRequired()])
    benefits = TextAreaField('Describe position benefits...', validators=[DataRequired()])
    salary = StringField('Position salary/wage: ', validators=[DataRequired()])

    submit = SubmitField('Submit Listing')

class ProfileForm(FlaskForm):
    phoneNumber = StringField('Phone number: ', validators=[DataRequired()])
    contactEmail = StringField('Email: ', validators=[DataRequired()])
    highSchool = StringField('High School: ', validators=[DataRequired()])
    university = StringField('College/University: ', validators=[DataRequired()])
    introduction = TextAreaField('Describe yourself...', validators=[DataRequired()])

    submit = SubmitField('Apply Changes')

class JobHistoryForm(FlaskForm):
    title = StringField('Previous position title: ', validators=[DataRequired()])
    companyName = StringField('Previous employer name: ', validators=[DataRequired()])
    startDate = DateField('Start Date: ', format = '%m/%d/%Y', validators=[DataRequired()])
    endDate = DateField('End Date: ', format = '%m/%d/%Y', validators=[DataRequired()])
    description = StringField('Describe your position: ', validators=[DataRequired()])

    submit = SubmitField('Apply Changes')

class ReferencesForm(FlaskForm):
    name = StringField("Full Name (Reference): ", validators=[DataRequired()])
    email = StringField("Email (Reference): ", validators=[DataRequired()])
    phoneNumber = StringField("Phone # (Reference): ", validators=[DataRequired()])
    organization = StringField("Organization (Reference): ", validators=[DataRequired()])

    submit = SubmitField('Apply Changes')


    
