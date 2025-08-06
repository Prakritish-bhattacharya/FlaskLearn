import dbm
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_sqlalchemy import SQLAlchemy


    
app = Flask(__name__)
app.secret_key = "osdfbn;"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#  create dataBase table
class FormData(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

with app.app_context():
    db.create_all()
#  Fileds , How meny fileds you are required
class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()] )
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET','POST'])
def index():
    form = MyForm()
    #  write HTTP methods while form uploading
    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        # save into database
        form_data = FormData(name = name, email = email)
        db.session.add(form_data)
        db.session.commit()
        return "success"
    return render_template('index.htmlk', form=form)
if __name__ == '__main__':
    app.run(debug=True)
    
