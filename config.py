import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'social_pool.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'iW4BfRdgSyxf'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

