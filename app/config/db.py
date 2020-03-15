from .. import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
database = os.environ['POSTGRES_DB']

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@database/%s' % (user, password, database)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

