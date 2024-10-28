from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#create a flask instance
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')   

#add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#secret key
app.config['SECRET_KEY'] = "Naidan"

db = SQLAlchemy(app)
with app.app_context():
    date_added = db.Column(db.DateTime, default=lambda: datetime.now(datetime.tiezone.utc))
#Create a model

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False) # nullable means it can't be empty
    email = db.Column(db.String(200), nullable = False, unique = True)
    date_added = db.Column(db.DateTime, default=datetime.now())
    # date_added = db.Column(db.DateTime, default = datetime.utcnow) // This method is now depreciated
    
    #create a string

    def __repr__(self):
        return '<Name %r>' % self.name
    
@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = Users.query.get_or_404(id)
    name = None
    form = UserForm()
    try: 
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("User Deleted Successfully")

        our_users = Users.query.order_by(Users.date_added)
        return render_template("add_user.html",
            form=form,
            name = None,
            our_users = our_users)
    except:
        flash("There was a problem deleting user try again")

        our_users = Users.query.order_by(Users.date_added)
        return render_template("add_user.html",
            form=form,
            name = None,
            our_users = our_users)


#create a form class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators = [DataRequired()])
    submit = SubmitField("Submit")

#Create another form class for user

class UserForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired()])
    submit = SubmitField("Submit")

#Update database record

@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)

    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        try:
            db.session.commit()
            flash(" User Updated Successfully ")
            return render_template("update.html",
            form = form,
            name_to_update = name_to_update)
        except:
            flash(" ERROR : User Update Failed")
            return render_template("update.html",
            form = form,
            name_to_update = name_to_update)
    else : 
            return render_template("update.html",
            form = form,
            name_to_update = name_to_update,
            id = id)



@app.route('/user/add', methods =['GET','POST'])
def add_user():
    form = UserForm()
    name = None

    if form.validate_on_submit():
        user = Users.query.filter_by(email = form.email.data).first() 
        # query the database grab all of the users that have the email address of whatever 
        # has been typed in and return the first one, it shouldnt return anything because it should be unique
        # this will look for the email address in the database

        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()

        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash("User added successfully")
    our_users = Users.query.order_by(Users.date_added)


    return render_template("add_user.html",
        form=form,
        name = None,
        our_users = our_users)

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
        flash("Form submitted succesfully")
    return render_template('name.html',
    name = name,
    form = form)



if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
