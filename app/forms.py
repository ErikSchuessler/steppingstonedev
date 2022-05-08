from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, IntegerField, SubmitField, PasswordField, SelectField, TextAreaField, RadioField, DateField
from wtforms.validators import DataRequired

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
    businessName = StringField('Name of Business: ', validators=[DataRequired()])
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
    phoneNumber = StringField('Phone number: ')
    contactEmail = StringField('Email: ')
    highSchool = StringField('High School: ')
    university = StringField('College/University: ')
    introduction = TextAreaField('Describe yourself...')

    submit = SubmitField('Apply Changes')

class JobHistoryForm(FlaskForm):
    id = IntegerField("Job History Number:")
    title = StringField('Previous position title: ', validators=[DataRequired()])
    companyName = StringField('Previous employer name: ')
    startDate = DateField('Start Date: ')
    endDate = DateField('End Date: ')
    description = StringField('Describe your position: ')

    submit = SubmitField('Apply Changes')

class ReferencesForm(FlaskForm):
    id = IntegerField('Id')
    name = StringField("Full Name (Reference): ", validators=[DataRequired()])
    email = StringField("Email (Reference): ", validators=[DataRequired()])
    phoneNumber = StringField("Phone Number (Reference): ", validators=[DataRequired()])
    organization = StringField("Organization (Reference): ", validators=[DataRequired()])

    submit = SubmitField('Apply Changes')

class SearchForm(FlaskForm):
    businessName = StringField('Business Name: ')
    city = StringField('City: ')
    state = StringField('State: ')

    submit = SubmitField('Search')


    
