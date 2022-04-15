from app import app
from flask import render_template, redirect, url_for
from app.forms import AddForm, DeleteForm, SearchForm, PopulationFilterForm, StudentRegistrationForm, BusinessRegistrationForm, ListingForm
from app import db
from app.models import City, User, Listing
import sys

@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/add_listing', methods=['GET', 'POST'])
def add_listing():
    form = ListingForm()
    if form.validate_on_submit():
        streetAddress = form.streetAddress.data
        city = form.city.data
        state = form.state.data
        zip = form.zip.data
        positionTitle = form.positionTitle.data
        qualifications = form.qualifications.data
        isInternship = bool(form.isInternship.data)
        isPartTime = bool(form.isPartTime.data)
        description = form. description.data
        benefits = form.benefits.data
        salary = form.salary.data

        listing = Listing(businessId = 2, streetAddress=streetAddress, city=city, state=state, zip=zip, positionTitle=positionTitle, qualifications=qualifications, isInternship=isInternship, isPartTime=isPartTime, description=description, benefits=benefits, salary=salary)
        db.session.add(listing)
        db.session.commit()
        return redirect(url_for('hello'))
    return render_template('add_listing.html', form=form)


@app.route('/registration')
def register():
    return render_template('registration.html')

@app.route('/student_registration', methods=['GET', 'POST'])
def student_registration():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        password = form.password.data
        role = 1
        
        student = User(firstName=firstName, lastName=lastName, email=email, password=password, role=role)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('hello'))
    return render_template('student_registration.html', form=form)




@app.route('/business_registration', methods=['GET', 'POST'])
def business_registration():
    form = BusinessRegistrationForm()
    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        businessName = form.businessName.data
        email = form.email.data
        password = form.password.data
        role = 2

        business = User(firstName=firstName, lastName=lastName, businessName=businessName, email=email, password=password, role=role)
        db.session.add(business)
        db.session.commit()
        return redirect(url_for('hello'))
    return render_template('business_registration.html', form=form)




@app.route('/add', methods=['GET', 'POST'])
def add_record():
    form = AddForm()
    if form.validate_on_submit():
        # Extract values from form
        city_name = form.city.data
        population = form.population.data

        # Create a city record to store in the DB
        c = City(city=city_name, population=population)

        # add record to table and commit changes
        db.session.add(c)
        db.session.commit()

        form.city.data = ''
        form.population.data = ''
        return redirect(url_for('add_record'))
    return render_template('add.html', form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete_record():
    form = DeleteForm()
    if form.validate_on_submit():
        # Query DB for matching record (we'll grab the first record in case
        # there's more than one).
        to_delete = db.session.query(City).filter_by(city = form.city.data).first()

        # If record is found delete from DB table and commit changes
        if to_delete is not None:
            db.session.delete(to_delete)
            db.session.commit()

        form.city.data = ''
        # Redirect to the view_all route (view function)
        return redirect(url_for('view'))
    return render_template('delete.html', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search_by_name():
    form = SearchForm()
    if form.validate_on_submit():
        # Query DB table for matching name
        record = db.session.query(City).filter_by(city = form.city.data).all()
        if record:
            return render_template('view_cities.html', cities=record)
        else:
            return render_template('not_found.html')
    return render_template('search.html', form=form)

@app.route('/view_all')
def view():
    all = db.session.query(City).all()
    print(all, file=sys.stderr)
    return render_template('view_cities.html', cities=all)

@app.route('/sort_by_name')
def sort_by_name():
    all = db.session.query(City).order_by(City.city).all()
    print(all, file=sys.stderr)
    return render_template('view_cities.html', cities=all)

@app.route('/filter_population', methods=['GET','POST'])
def filter_population():
    form = PopulationFilterForm()
    if form.validate_on_submit():
        min_population = form.population.data
        record = db.session.query(City).filter(City.population >= min_population).all()
        if record:
            return render_template('view_cities.html', cities=record)
        else:
            return render_template('not_found.html')
    return render_template('filter_populations.html', form=form)
    
    
