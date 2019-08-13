import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    UPLOADED_PHOTOS_DEST ='app/static/img'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mel123@localhost/blog'
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mel123@localhost/blog'
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mel123@localhost/blog'
    DEBUG = True

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config:The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mel123@localhost/blogr'
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

