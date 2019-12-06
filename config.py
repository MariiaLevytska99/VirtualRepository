class Config(object):
    """
    Base Configuration Class
    Contains all Application Constant
    Defaults
    """
    # Flask Settings
    DEBUG = False
    IS_PRODUCTION = False
    IS_STAGING = False

    # db_host = 'localhost'
    # db_user = 'root'
    # db_pass = '123456789'
    # db_name = 'bootcamp'

    db_host = 'remotemysql.com'
    db_host = 'remotemysql.com'
    db_user = '1IWKkGUs6z'
    db_pass = '5wKwhA7bzm'
    db_name = '1IWKkGUs6z'

    # Database Settings
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(db_user, db_pass, db_host, db_name)
    SQLALCHEMY_POOL_RECYCLE = 500
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 10

    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'soully'

