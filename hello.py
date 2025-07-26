from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash to work


@app.route('/')
def registration():
    # return render_template('formfetch.html')
    return render_template('formfile.html')

@app.route('/success', methods = ['POST'])
def printdata():
    result = request.form
    return render_template('success.html', result = result)

@app.route('/filesubmit', methods = ['POST'])
def filesubmit():
    f = request.files['file']
    f.save('static/'+f.filename)
    return "success"
    # return re