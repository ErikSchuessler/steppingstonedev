from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import (
    AddForm, 
    DeleteForm, 
    SearchForm, 
    PopulationFilterForm, 
    LoginForm, 
    StudentRegistrationForm, 
    BusinessRegistrationForm, 
    ListingForm, 
    ProfileForm, 
    JobHistoryForm, 
    ReferencesForm
)
from app import db
from app.models import City, User, Listing, Profile, JobHistory, Reference
import sys

@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Authenticated users are redirected to home page.
    if current_user.is_authenticated:
        return redirect(url_for('hello'))
    form = LoginForm()
    if form.validate_on_submit():
        # Query DB for user by username
        user = db.session.query(User).filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            print('Login failed', file=sys.stderr)
            return redirect(url_for('login'))
        # login_user is a flask_login function that starts a session
        login_user(user)
        print('Login successful', file=sys.stderr)
        return redirect(url_for('hello'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('hello'))

@app.route('/profile')
def profile():
    userProfile = db.session.query(Profile).filter_by(userId = current_user.id).first()
    return render_template('profile.html', Profile=userProfile)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    print('edit profile')
    profileForm = ProfileForm()
    userProfile = db.session.query(Profile).filter_by(userId = current_user.id).first()
    if profileForm.validate_on_submit():
        #add new profile logic here, when userProfile is null, we have to add user
        if userProfile == None: 
            userProfile = Profile()
            userProfile.userId = current_user.id
            db.session.add(userProfile)
             
        userProfile.phoneNumber = profileForm.phoneNumber.data
        userProfile.contactEmail = profileForm.contactEmail.data
        userProfile.highSchool = profileForm.highSchool.data
        userProfile.university = profileForm.university.data
        userProfile.introduction = profileForm.introduction.data
          
        print('just before commit' + str(userProfile.id))
        db.session.commit()
        return redirect(url_for('profile'))
    else:
        
        return render_template('edit_profile.html', profileForm= ProfileForm(), profile = userProfile)


@app.route('/add_reference', methods=['GET','POST'])
def add_reference():
    referencesForm = ReferencesForm()

    if referencesForm.validate_on_submit():
        name = referencesForm.name.data
        email = referencesForm.email.data
        phoneNumber = phoneNumber.referencesForm.data
        organization = organization.referencesForm.data

        reference = Reference(profiledId=1, name=name, email=email, phoneNumber=phoneNumber, organization=organization)
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('add_reference.html')

@app.route('/add_job_history', methods=['GET','POST'])
def add_job_history():
    jobHistoryForm = JobHistoryForm()

    if jobHistoryForm.validate_on_submit():
        title = jobHistoryForm.name.data
        companyName = jobHistoryForm.email.data
        startDate = phoneNumber.jobHistoryForm.data
        endDate = organization.jobHistoryForm.data
        description = description

        jobHistory = JobHistory(profiledId=1, name=name, email=email, phoneNumber=phoneNumber, organization=organization)
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('hello'))
    return render_template('add_reference.html')


    

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

@app.route('/view_listings', methods=['GET', 'POST'])
def view_listings():
    all = db.session.query(Listing).all()
    print(all, file=sys.stderr)
    return render_template('view_listings.html', Listings=all)



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
        password = generate_password_hash(form.password.data)
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
    
    
