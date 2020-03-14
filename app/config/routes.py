from .. import app
from .. import views


app.add_url_rule('/', view_func=views.home)

