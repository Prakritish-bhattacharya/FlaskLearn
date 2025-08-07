from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, Email

# import form  # we imported 4 required functions from wtforms.validators for wtforms validation

app = Flask(__name__)
app.secret_key = "fhv"  # here we need secret_key for CSRF token
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mytry.db'
db = SQLAlchemy(app)

# .................create database table..................
class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable = False, unique = True)
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
        
        # save data into db
        form_data = FormData(name = name , email = email, phone =  phone)
        db.session.add(form_data)
        db.session.commit()
        return "success"
        
    return render_template('index.html', sendToFrontedForm = FrontendForm)
    
    
if __name__ == '__main__':
    app.run( debug = True )