# app/models.py
from app import db

class Teacher(db.Model):
    id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Integer, nullable=False)

    papers = db.relationship('TeacherPaper', back_populates='teacher')
    courses = db.relationship('TeacherCourse', back_populates='teacher')
    projects = db.relationship('TeacherProject', back_populates='teacher')


class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    source = db.Column(db.String(256), nullable=False)
    year = db.Column(db.Date, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)

    authors = db.relationship('TeacherPaper', back_populates='paper')


class Course(db.Model):
    id = db.Column(db.String(256), primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    nature = db.Column(db.Integer, nullable=False)

    teachers = db.relationship('TeacherCourse', back_populates='course')


class Project(db.Model):
    id = db.Column(db.String(256), primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    source = db.Column(db.String(256), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    total_funding = db.Column(db.Float, nullable=False)
    start_year = db.Column(db.Integer, nullable=False)
    end_year = db.Column(db.Integer, nullable=False)

    teachers = db.relationship('TeacherProject', back_populates='project')


class TeacherPaper(db.Model):
    teacher_id = db.Column(db.String(5), db.ForeignKey('teacher.id'), primary_key=True)
    paper_id = db.Column(db.Integer, db.ForeignKey('paper.id'), primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    is_corresponding_author = db.Column(db.Boolean, nullable=False)

    teacher = db.relationship('Teacher', back_populates='papers')
    paper = db.relationship('Paper', back_populates='authors')


class TeacherCourse(db.Model):
    teacher_id = db.Column(db.String(5), db.ForeignKey('teacher.id'), primary_key=True)
    course_id = db.Column(db.String(256), db.ForeignKey('course.id'), primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    hours_taken = db.Column(db.Integer, nullable=False)

    teacher = db.relationship('Teacher', back_populates='courses')
    course = db.relationship('Course', back_populates='teachers')


class TeacherProject(db.Model):
    teacher_id = db.Column(db.String(5), db.ForeignKey('teacher.id'), primary_key=True)
    project_id = db.Column(db.String(256), db.ForeignKey('project.id'), primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    funding_taken = db.Column(db.Float, nullable=False)

    teacher = db.relationship('Teacher', back_populates='projects')
    project = db.relationship('Project', back_populates='teachers')
