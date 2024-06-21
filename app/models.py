from app import db

class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    authors = db.Column(db.String(256), nullable=False)
    journal = db.Column(db.String(256), nullable=False)
    year = db.Column(db.Integer, nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    lead = db.Column(db.String(256), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    teacher = db.Column(db.String(256), nullable=False)
    semester = db.Column(db.String(256), nullable=False)
