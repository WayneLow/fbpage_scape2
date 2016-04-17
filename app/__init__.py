from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database and login_manager object
db = SQLAlchemy(app)

# Sample HTTP error handling
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
# from app.mod_auth.controllers import mod_auth as auth_module
from app.content import views, models

# Register blueprint(s)
# app.register_blueprint(auth_module)


# Build the database:
# This will create the database file using SQLAlchemy
# with app.app_context():
#     db.create_all()
