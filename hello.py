from flask import Flask, abort, render_template, request, redirect, flash, url_for

app = Flask(__name__)
# use secret key for flashing
app.secret_key = "I love you"

@app.route('/form', methods =['POST','GET'])
def handle_form():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        return redirect(url_for('success',  name = name , email = email))
    return render_template('form.html')

@app.route('/success')
def success():
    
    name = request.args.get('name')
    email = request.args.get('email')
    return render_template('success.html', name = name, email = email)