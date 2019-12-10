import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://pavlo:grib@localhost/DataManagment?host=localhost?port=3306'
    SQLALCHEMY_TRACK_MODIFICATIONS = False