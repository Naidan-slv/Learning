from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


#create a flask instance
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')   
app.config['SECRET_KEY'] = "Naidan"

#create a form class

class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators = [DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')

#create name page 
@app.route('/name', methods =['GET','POST' ])
def name():
    name = None
    form = NamerForm()
    #Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('name.html',
    name = name,
    form = form)



if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
