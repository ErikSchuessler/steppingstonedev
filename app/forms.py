from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, TextAreaField, RadioField
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

class StudentRegistrationForm(FlaskForm):
    firstName = StringField('First name:', validators=[DataRequired()])
    lastName = StringField('Last name:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    password = StringField('Password:', validators=[DataRequired()])
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

    
