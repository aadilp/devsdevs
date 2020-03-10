from flask import Flask
app = Flask(__name__)
from app import views
app.add_url_rule('/', view_func=views.home)

