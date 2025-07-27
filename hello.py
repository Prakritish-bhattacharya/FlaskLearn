# app.py
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
# from forms import UserForm
from form import UserForm
from models import db, User
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('User added successfully!')
        return redirect(url_for('home'))
    return render_template('home.html', form=form)
