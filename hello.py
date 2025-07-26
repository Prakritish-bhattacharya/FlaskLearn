from flask import Flask, abort, render_template, request, redirect, flash, url_for

app = Flask(__name__)
# use secret key for flashing
app.secret_key = "I love you"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')