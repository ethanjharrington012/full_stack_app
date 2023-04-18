import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """
    Sets config variable for the flask app.
    using Envirnment variable where available otherwise 
    creat the config variable if not done already
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or "YOU will never guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+ os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIDICATIONS = False #turn off update messages from sqlalchemy



