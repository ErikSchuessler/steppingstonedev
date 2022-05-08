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
    ReferencesForm,
    SearchForm
)
from app import db
from app.models import User, Listing, Profile, JobHistory, Reference, Application
import sys

@app.route('/')
def hello():
    return render_template('homepage.html')

def is_student():

    # determines if authenticated user is a student user.

    if current_user:
        if current_user.role == 1:
            return True
        else:
            return False
    else:
        print('User not authenticated.', file=sys.stderr)
        return redirect(url_for('hello'))

def is_business():

    # determines if authenticated user is business user.

    if current_user:
        if current_user.role == 2:
            return True
        else:
            return False
    else:
        print('User not authenticated.', file=sys.stderr)
        return redirect(url_for('hello'))

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


@app.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    listings = db.session.query(Listing)
    allApplications = db.session.query(Application).all()
    profile = db.session.query(Profile).filter_by(userId = current_user.id).first()
    if form.validate_on_submit():
        if form.businessName.data:
            listings = listings.filter_by(businessName = form.businessName.data)
        if form.city.data:
            listings = listings.filter_by(city = form.city.data)
        if form.state.data:
            listings = listings.filter_by(state = form.state.data)

        results = listings.all()
        if results:
            return render_template('view_listings.html', Listings=results, Applications=allApplications, ProfileId = profile.id)
        else:
            return render_template('error.html')
    return render_template('search.html', form=form)


@app.route('/view_profile/<profileId>')
def view_profile(profileId):
    
    userProfile = db.session.query(Profile).filter_by(id=profileId).first()
    user = db.session.query(User).filter_by(id=userProfile.userId).first()
    if userProfile is None:
        return render_template('error.html')
    else:
        userJobHistories = db.session.query(JobHistory).filter_by(profileId = userProfile.id).all()
        userReferences = db.session.query(Reference).filter_by(profileId = userProfile.id).all()
        return render_template('view_profile.html', Profile=userProfile, User = user, JobHistories = userJobHistories, References = userReferences)

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
    userProfile = db.session.query(Profile).filter_by(userId = current_user.id).first()
    
    if referencesForm.validate_on_submit():
        profileId = userProfile.id
        name = referencesForm.name.data
        email = referencesForm.email.data
        phoneNumber = referencesForm.phoneNumber.data
        organization = referencesForm.organization.data

        reference = Reference(profileId=profileId, name=name, email=email, phoneNumber=phoneNumber, organization=organization)
        db.session.add(reference)
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('add_reference.html', referencesForm=referencesForm)

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

@app.route('/edit_reference', methods=['GET', 'POST'])
def edit_reference():
    referencesForm=ReferencesForm()
    userProfile = db.session.query(Profile).filter_by(userId = current_user.id).first()
    print(referencesForm.id.data)
    if referencesForm.validate_on_submit():
        userReference = db.session.query(Reference).filter_by(id = referencesForm.id.data).first()
        userReference.name = referencesForm.name.data
        userReference.phoneNumber = referencesForm.phoneNumber.data
        userReference.email = referencesForm.email.data
        userReference.organization = referencesForm.organization.data 
        db.session.commit()
        return redirect(url_for('profile'))
    else:
        referenceId = request.args.get('referenceid')
        userReference = db.session.query(Reference).filter_by(id = referenceId).first()
        return render_template('edit_reference.html', referencesForm= ReferencesForm(), reference = userReference, profile = userProfile, errors = referencesForm.errors)

@app.route('/delete_reference', methods=['GET', 'POST'])
def delete_reference():
    referenceId = request.args.get('referenceid')
    userReference = db.session.query(Reference).filter_by(id = referenceId).first()
    db.session.delete(userReference)
    db.session.commit()
    return redirect(url_for('profile'))

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    listingId = request.args.get('listingId')
    print('*******************************************' + str(listingId))
    profile = db.session.query(Profile).filter_by(userId = current_user.id).first()
    print('*******************************************' + str(profile.id))
    application = Application(profileId=profile.id, listingId=listingId)
    db.session.add(application)
    db.session.commit()
    return redirect(url_for('view_listings'))
    
@app.route('/add_listing', methods=['GET', 'POST'])
def add_listing():
    if is_business():
        form = ListingForm()

        if form.validate_on_submit():
            businessName = form.businessName.data
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

            listing = Listing(businessId = current_user.id, businessName = businessName, streetAddress=streetAddress, city=city, state=state, zip=zip, positionTitle=positionTitle, qualifications=qualifications, isInternship=isInternship, isPartTime=isPartTime, description=description, benefits=benefits, salary=salary)
            db.session.add(listing)
            db.session.commit()
            return redirect(url_for('hello'))
        return render_template('add_listing.html', form=form)
    else:
        return render_template('unauthorized.html')

@app.route('/view_listings', methods=['GET', 'POST'])
def view_listings():
    allListings = db.session.query(Listing).all()
    allApplications = db.session.query(Application).all()
    profile = db.session.query(Profile).filter_by(userId = current_user.id).first()
    print(allListings, file=sys.stderr)
    return render_template('view_listings.html', Listings=allListings, Applications=allApplications, ProfileId = profile.id)

@app.route('/my_listings', methods=['GET', 'POST'])
def my_listings():
    myListings = db.session.query(Listing).filter_by(businessId = current_user.id).all()
    allApplications = db.session.query(Application).all()
    studentUsers = db.session.query(User).all()
    allProfiles = db.session.query(Profile).all()
    return render_template('my_listings.html', Listings=myListings, Applications=allApplications, StudentUsers = studentUsers, Profiles = allProfiles)

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
        db.session.refresh(student)
        
        profile = Profile(userId=student.id, phoneNumber='', contactEmail='', highSchool='', university='', introduction='')
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('student_registration.html', form=form)

@app.route('/business_registration', methods=['GET', 'POST'])
def business_registration():
    form = BusinessRegistrationForm()
    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        businessName = form.businessName.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        role = 2

        business = User(firstName=firstName, lastName=lastName, businessName=businessName, email=email, password=password, role=role)
        db.session.add(business)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('business_registration.html', form=form)







    
    
