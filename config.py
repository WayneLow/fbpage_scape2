import os

# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
# DATABASE_NAME = 'testdb'
# SQLALCHEMY_DATABASE_URI = 'postgresql:///' + DATABASE_NAME
# DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')


# Facebook and Twitter token
OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '546664045494484',
        'secret': '881d170f5bf1b8c7c396faeb56a22dd9'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}


# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "k6dyeYM999JsXSKR*Q!tus6G3MDp29X6"

UNI_LIST = {
    'utar': '306608096208936',
    'sunway': '289984354471103',
    'taylor': '363942057090970',
    'kdu': 'KDUConfessionsPage',
    'segi': 'SegiUniversityCollegeConfessionsSUCC'}
