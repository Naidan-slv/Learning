from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.testdb.db'

    db.init_app(app)

    from views import register_routes

    migrate = Migrate(app, db)
    return app

# in the function we want to do the import in the function this lets us avoid circular imports
# we need to do migrate and update every time we make a change to the models
# we only need to do db init once
