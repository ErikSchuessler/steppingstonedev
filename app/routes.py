from app import app
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import (
    LoginForm, 
    StudentRegistrationForm, 
    BusinessRegistrationForm, 
    ListingForm, 
    ProfileForm, 
    JobHistoryForm, 
    ReferencesForm
)
from app import db
from app.models import User, Listing, Profile, JobHistory, Reference
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
    if userProfile is None:
        return render_template('profile.html', Profile=userProfile)
    else:
        userJobHistories = db.session.query(JobHistory).filter_by(profileId = userProfile.id).all()
        userReferences = db.session.query(Reference).filter_by(profileId = userProfile.id).all()
        return render_template('profile.html', Profile=userProfile, JobHistories = userJobHistories, References = userReferences)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    profileForm = ProfileForm()
    userProfile = db.session.query(Profile).filter_by(userId = current_user.id).first()
    if profileForm.validate_on_submit():
        if userProfile == None: 
            userProfile = Profile()
            userProfile.userId = current_user.id
            db.session.add(userProfile)
             
        userProfile.phoneNumber = profileForm.phoneNumber.data
        userProfile.contactEmail = profileForm.contactEmail.data
        userProfile.highSchool = profileForm.highSchool.data
        userProfile.university = profileForm.university.data
        userProfile.introduction = profileForm.introduction.data
          
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
    userProfile = db.session.query(Profile).filter_by(userId = current_user.id).first()

    if jobHistoryForm.validate_on_submit():
        profileId = userProfile.id
        title = jobHistoryForm.title.data
        companyName = jobHistoryForm.companyName.data
        startDate = jobHistoryForm.startDate.data
        endDate = jobHistoryForm.endDate.data
        description = jobHistoryForm.description.data
        jobHistory = JobHistory(profileId=profileId, title=title, companyName=companyName, startDate=startDate, endDate=endDate, description=description)
        db.session.add(jobHistory)
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('add_job_history.html', jobHistoryForm=jobHistoryForm)

@app.route('/edit_job_history', methods=['GET','POST'])
def edit_job_history():
    jobHistoryForm = JobHistoryForm()
    userProfile = db.session.query(Profile).filter_by(userId = current_user.id).first()
  
    if jobHistoryForm.is_submitted():
        print("submitted")

    if jobHistoryForm.validate():
        print("valid")
    else:
        print(jobHistoryForm.errors)

    if jobHistoryForm.validate_on_submit():
        userJobHistory = db.session.query(JobHistory).filter_by(id = jobHistoryForm.id.data).first()
        userJobHistory.title = jobHistoryForm.title.data
        userJobHistory.companyName = jobHistoryForm.companyName.data
        userJobHistory.startDate = jobHistoryForm.startDate.data
        userJobHistory.endDate = jobHistoryForm.endDate.data
        userJobHistory.description = jobHistoryForm.description.data      
        db.session.commit()
        return redirect(url_for('profile'))
    else:
        jobId = request.args.get('jobid')
        userJobHistory = db.session.query(JobHistory).filter_by(id = jobId).first()
        return render_template('edit_job_history.html', jobHistoryForm= JobHistoryForm(), job = userJobHistory, profile = userProfile, errors = jobHistoryForm.errors)

@app.route('/delete_job_history', methods=['GET','POST'])
def delete_job():
    #jobHistoryForm = JobHistoryForm()
    jobId = request.args.get('jobid')

    userJobHistory = db.session.query(JobHistory).filter_by(id = jobId).first()
    #print(jobHistoryForm.id.data)
    db.session.delete(userJobHistory)
    db.session.commit()
    return redirect(url_for('profile'))
    
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







    
    
