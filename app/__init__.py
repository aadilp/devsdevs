from flask import Flask
app = Flask(__name__)

from .config import routes
from .config.db import db, migrate
from .models import appuser

