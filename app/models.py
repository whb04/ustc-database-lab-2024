# app/models.py
from app import db
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint, UniqueConstraint

class Teacher(db.Model):
    id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Integer, nullable=False)

    papers = db.relationship('TeacherPaper', back_populates='teacher')
    courses = db.relationship('TeacherCourse', back_populates='teacher')
    projects = db.relationship('TeacherProject', back_populates='teacher')

    __table_args__ = (
        CheckConstraint('gender IN (1, 2)', name='check_teacher_gender'),
        CheckConstraint('title IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)', name='check_teacher_title')
    )

class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    source = db.Column(db.String(256), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)

    authors = db.relationship('TeacherPaper', back_populates='paper')

    __table_args__ = (
        CheckConstraint('type IN (1, 2, 3, 4)', name='check_paper_type'),
        CheckConstraint('level IN (1, 2, 3, 4, 5, 6)', name='check_paper_level'),
    )

class TeacherPaper(db.Model):
    teacher_id = db.Column(db.String(5), db.ForeignKey('teacher.id'), primary_key=True)
    paper_id = db.Column(db.Integer, db.ForeignKey('paper.id'), primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    is_corresponding_author = db.Column(db.Boolean, nullable=False)

    teacher = db.relationship('Teacher', back_populates='papers')
    paper = db.relationship('Paper', back_populates='authors')

    __table_args__ = (
        UniqueConstraint('paper_id', 'rank', name='unique_paper_rank'),
    )

    @validates('is_corresponding_author')
    def validate_corresponding_author(self, key, value):
        if value:
            corresponding_authors = TeacherPaper.query.filter_by(paper_id=self.paper_id, is_corresponding_author=True).count()
            if corresponding_authors > 0:
                raise ValueError('A paper can only have one corresponding author')
        return value

class Course(db.Model):
    id = db.Column(db.String(256), primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    nature = db.Column(db.Integer, nullable=False)

    teachers = db.relationship('TeacherCourse', back_populates='course')

    __table_args__ = (
        CheckConstraint('nature IN (1, 2)', name='check_course_nature'),
    )

class TeacherCourse(db.Model):
    teacher_id = db.Column(db.String(5), db.ForeignKey('teacher.id'), primary_key=True)
    course_id = db.Column(db.String(256), db.ForeignKey('course.id'), primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    semester = db.Column(db.Integer, primary_key=True)
    hours_taken = db.Column(db.Integer, nullable=False)

    teacher = db.relationship('Teacher', back_populates='courses')
    course = db.relationship('Course', back_populates='teachers')

    __table_args__ = (
        CheckConstraint('semester IN (1, 2, 3)', name='check_course_semester'),
    )

    @validates('hours_taken')
    def validate_hours_taken(self, key, value):
        if value:
            total_hours = db.session.query(db.func.sum(TeacherCourse.hours_taken)).filter_by(course_id=self.course_id, year=self.year, semester=self.semester).scalar()
            if total_hours is None:
                total_hours = 0
            course_hours = Course.query.filter_by(id=self.course_id).first().hours
            if total_hours + value > course_hours:
                raise ValueError('Total teaching hours cannot exceed course hours')
        return value

class Project(db.Model):
    id = db.Column(db.String(256), primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    source = db.Column(db.String(256), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    total_funding = db.Column(db.Float, nullable=False)
    start_year = db.Column(db.Integer, nullable=False)
    end_year = db.Column(db.Integer, nullable=False)

    teachers = db.relationship('TeacherProject', back_populates='project')

    __table_args__ = (
        CheckConstraint('type IN (1, 2, 3, 4, 5)', name='check_project_type'),
    )

class TeacherProject(db.Model):
    teacher_id = db.Column(db.String(5), db.ForeignKey('teacher.id'), primary_key=True)
    project_id = db.Column(db.String(256), db.ForeignKey('project.id'), primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    funding_taken = db.Column(db.Float, nullable=False)

    teacher = db.relationship('Teacher', back_populates='projects')
    project = db.relationship('Project', back_populates='teachers')

    __table_args__ = (
        UniqueConstraint('project_id', 'rank', name='unique_project_rank'),
    )

    @validates('funding_taken')
    def validate_funding_taken(self, key, value):
        if value:
            total_funding = db.session.query(db.func.sum(TeacherProject.funding_taken)).filter_by(project_id=self.project_id).scalar()
            if total_funding is None:
                total_funding = 0
            project_funding = Project.query.filter_by(id=self.project_id).first().total_funding
            if total_funding + value > project_funding:
                raise ValueError('Total funding taken cannot exceed project total funding')
        return value
