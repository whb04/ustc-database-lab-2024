import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1@localhost/lab3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # 用于Flask-WTF保护表单
