from dotenv import load_dotenv
import os


project_folder = os.path.abspath(os.getcwd())
load_dotenv(os.path.join(project_folder, '.env'))

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///DB.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    secret_key = os.getenv("SECRET_KEY")
