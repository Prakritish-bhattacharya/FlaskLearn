from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash to work

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['username']
        if name:  # basic validation
            flash(f"Welcome, {name}!", "success")
            return redirect(url_for('index'))
        else:
            flash("Name cannot be empty!", "error")
            return redirect(url_for('index'))

    return render_template('index.html')
