from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError


app = Flask(__name__)
app.secret_key = "osdfbn;"

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()] )
    submit = SubmitField('Submit')

@app.route('/')
def index():
    form = MyForm()
    return render_template('index.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/app1')
def app1():
    return "<h1>;ovhk.vzbj;vikh[0o;d9ivlhneo;fiv, m'dnoagflvneoairlghvb;k</h1>"