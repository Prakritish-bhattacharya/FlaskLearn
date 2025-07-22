from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contactus():
    return render_template('contactus.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/success')
def success():
    return render_template('success.html')