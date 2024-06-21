from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models import Paper, Project, Course
from app.forms import PaperForm, ProjectForm, CourseForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/papers', methods=['GET', 'POST'])
def papers():
    form = PaperForm()
    if form.validate_on_submit():
        paper = Paper(
            title=form.title.data,
            authors=form.authors.data,
            journal=form.journal.data,
            year=form.year.data
        )
        db.session.add(paper)
        db.session.commit()
        flash('Paper added successfully!')
        return redirect(url_for('papers'))
    papers = Paper.query.all()
    return render_template('papers.html', form=form, papers=papers)

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            lead=form.lead.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data
        )
        db.session.add(project)
        db.session.commit()
        flash('Project added successfully!')
        return redirect(url_for('projects'))
    projects = Project.query.all()
    return render_template('projects.html', form=form, projects=projects)

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    form = CourseForm()
    if form.validate_on_submit():
        course = Course(
            title=form.title.data,
            teacher=form.teacher.data,
            semester=form.semester.data
        )
        db.session.add(course)
        db.session.commit()
        flash('Course added successfully!')
        return redirect(url_for('courses'))
    courses = Course.query.all()
    return render_template('courses.html', form=form, courses=courses)
