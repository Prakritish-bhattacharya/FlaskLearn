import os
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import EmailField, FileField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, Email, EqualTo
from flask_wtf.file import FileAllowed , FileRequired, FileField
from werkzeug.utils import secure_filename

# import form  # we imported 4 required functions from wtforms.validators for wtforms validation

app = Flask(__name__)
app.secret_key = "fhv"  # here we need secret_key for CSRF token
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fileUpload.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max 16MB upload
db = SQLAlchemy(app)

# .................create database Model..................
class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable = False, unique = True)
    file = db.Column(db.String(100), nullable=False)
# use app_context for create the table
with app.app_context():
    db.create_all()
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100))
# use app_context for create the table
with app.app_context():
    db.create_all()

#  ....................create required form.....................
class MyForm(FlaskForm):  #pass FlaskForm for flask form validation
    name = StringField('Name :', validators=[DataRequired()]) 
    email = EmailField('Email', validators= [DataRequired(), Email()])
    phone = StringField('Phone No :', validators= [
        DataRequired( message = "phone number is required."),
        Length(min = 10, max = 11, message="Phone number must be between 10 and 15 digits."),
        Regexp(r'^\+?[0-9]{10,15}$', message="Enter a valid phone number.")
        ])
    file = FileField('Upload File', validators=[
        FileRequired(), 
        FileAllowed(['jpg','png','pdf','txt','gif'], 'only images or documents allowed') 
    ])
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    name = StringField('user name:', validators=[DataRequired()])
    email = EmailField('Email', validators= [DataRequired(), Email()])
    # create strong validation in password
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm', message='Passwords must match'),
        Length(min=8, max=50, message='Password must be between 8 and 50 characters'),
        ])
    # confirm password
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
 
#  create Route for form
@app.route('/wtform', methods = ['GET','POST'])
def index():
    FrontendForm = MyForm()
    
    #  check HTTP methods while form are submitted
    if request.method == "POST" and FrontendForm.validate_on_submit():
        name = FrontendForm.name.data  # take all data from form field
        email = FrontendForm.email.data
        phone = FrontendForm.phone.data
        uploaded_file = FrontendForm.file.data
        filename = secure_filename(uploaded_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)
        
        # save data into db
        form_data = FormData(name = name , email = email, phone =  phone, file = filename)
        db.session.add(form_data)
        db.session.commit()
        return "success"
        
    return render_template('index.html', sendToFrontedForm = FrontendForm)



#  show db data
@app.route('/formdata')
def formData():
    formDt = FormData.query.all()
    return render_template('formdata.html123', formDt = formDt )

@app.route('/users/<int:id>/edit', methods = ['GET','POST'])
def edit(id):
    formData = FormData.query.get(id)
    form = MyForm(obj = formData)
    # formIns = MyForm()
    if form.validate_on_submit():
        formData.name = form.name.data
        formData.email = form.email.data
        formData.phone = form.phone.data
        db.session.commit()
        return redirect(url_for('formData'))
    return render_template('edit.html', formData = formData, form = form)
    
    

    
    
    
    
    
    
    
    
    
    
@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('auth/register.html', form = form)
if __name__ == '__main__':
    app.run( debug = True )