#!/usr/bin/env python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config.from_object('config')
db = SQLAlchemy(app)



basedir = "/home/cheonying/Repos/Wayne/fbpage_scape2/"
conffile = basedir+"emonhub.conf"

@app.route('/')
def index():
    with open(basedir+"index.html", 'rb') as f:
        content = f.read()
    return content

# ------------------------------------------------------------------------------------    
# MAIN PROGRAM
# ------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
