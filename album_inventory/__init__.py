from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .models import db as root_db, login_manager, ma

from flask_migrate import Migrate

# flask CORS import = CROSS ORIGIN RESOURCE SHAREING - future proofing
# our reach app so it makes it this flask app
from flask_cors import CORS


app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)
root_db.init_app(app)

migrate = Migrate(app, root_db)

ma.init_app(app)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

CORS(app)
