# app/routes.py

from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.models import Teacher, Paper, Course, Project, TeacherPaper, TeacherCourse, TeacherProject
from app.forms import TeacherForm, PaperForm, CourseForm, ProjectForm

@app.route('/')
def index():
    return render_template('index.html')

# Teacher routes
@app.route('/teachers', methods=['GET', 'POST'])
def teachers():
    teachers = Teacher.query.all()
    return render_template('teachers.html', teachers=teachers)

@app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    form = TeacherForm()
    if form.validate_on_submit():
        teacher = Teacher(
            id=form.id.data,
            name=form.name.data,
            gender=form.gender.data,
            title=form.title.data
        )
        try:
            db.session.add(teacher)
            db.session.commit()
            flash('Teacher added successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding teacher: {e}', 'danger')
        return redirect(url_for('teachers'))
    return render_template('add_teacher.html', form=form)

@app.route('/edit_teacher/<string:teacher_id>', methods=['GET', 'POST'])
def edit_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    form = TeacherForm(obj=teacher)
    if form.validate_on_submit():
        try:
            # Update the teacher with new form data
            teacher.id = form.id.data
            teacher.name = form.name.data
            teacher.gender = form.gender.data
            teacher.title = form.title.data
            db.session.commit()
            flash('Teacher updated successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating teacher: {e}', 'danger')
        return redirect(url_for('teachers'))
    return render_template('edit_teacher.html', form=form)

@app.route('/delete_teacher/<string:teacher_id>', methods=['POST'])
def delete_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    try:
        db.session.delete(teacher)
        db.session.commit()
        flash('Teacher deleted successfully!')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting teacher: {e}', 'danger')
    return redirect(url_for('teachers'))

# Paper routes
@app.route('/papers', methods=['GET', 'POST'])
def papers():
    form = PaperForm()
    if form.validate_on_submit():
        try:
            paper = Paper(
                id=form.id.data,
                title=form.title.data,
                source=form.source.data,
                year=form.year.data,
                type=form.type.data,
                level=form.level.data
            )
            db.session.add(paper)
            db.session.commit()
            flash('Paper added successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding paper: {e}', 'danger')
        return redirect(url_for('papers'))
    papers = Paper.query.all()
    return render_template('papers.html', form=form, papers=papers)

# Course routes
@app.route('/courses', methods=['GET', 'POST'])
def courses():
    form = CourseForm()
    if form.validate_on_submit():
        try:
            course = Course(
                id=form.id.data,
                title=form.title.data,
                hours=form.hours.data,
                nature=form.nature.data
            )
            db.session.add(course)
            db.session.commit()
            flash('Course added successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding course: {e}', 'danger')
        return redirect(url_for('courses'))
    courses = Course.query.all()
    return render_template('courses.html', form=form, courses=courses)

# Project routes
@app.route('/projects', methods=['GET', 'POST'])
def projects():
    form = ProjectForm()
    if form.validate_on_submit():
        try:
            project = Project(
                id=form.id.data,
                title=form.title.data,
                source=form.source.data,
                type=form.type.data,
                total_funding=form.total_funding.data,
                start_year=form.start_year.data,
                end_year=form.end_year.data
            )
            db.session.add(project)
            db.session.commit()
            flash('Project added successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding project: {e}', 'danger')
        return redirect(url_for('projects'))
    projects = Project.query.all()
    return render_template('projects.html', form=form, projects=projects)

# Edit Paper
@app.route('/edit_paper/<int:paper_id>', methods=['GET', 'POST'])
def edit_paper(paper_id):
    paper = Paper.query.get_or_404(paper_id)
    form = PaperForm(obj=paper)
    if form.validate_on_submit():
        try:
            # Update the paper with new form data
            paper.id = form.id.data
            paper.title = form.title.data
            paper.source = form.source.data
            paper.year = form.year.data
            paper.type = form.type.data
            paper.level = form.level.data
            db.session.commit()
            flash('Paper updated successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating paper: {e}', 'danger')
        return redirect(url_for('papers'))
    return render_template('edit_paper.html', form=form)


# Delete Paper
@app.route('/delete_paper/<int:paper_id>', methods=['POST'])
def delete_paper(paper_id):
    try:
        paper = Paper.query.get_or_404(paper_id)
        db.session.delete(paper)
        db.session.commit()
        flash('Paper deleted successfully!')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting paper: {e}', 'danger')
    return redirect(url_for('papers'))

# Edit Course
@app.route('/edit_course/<string:course_id>', methods=['GET', 'POST'])
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    form = CourseForm(obj=course)
    if form.validate_on_submit():
        try:
            # Update the course with new form data
            course.id = form.id.data
            course.title = form.title.data
            course.hours = form.hours.data
            course.nature = form.nature.data
            db.session.commit()
            flash('Course updated successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating course: {e}', 'danger')
        return redirect(url_for('courses'))
    return render_template('edit_course.html', form=form)

# Delete Course
@app.route('/delete_course/<string:course_id>', methods=['POST'])
def delete_course(course_id):
    try:
        course = Course.query.get_or_404(course_id)
        db.session.delete(course)
        db.session.commit()
        flash('Course deleted successfully!')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting course: {e}', 'danger')
    return redirect(url_for('courses'))

# Edit Project
@app.route('/edit_project/<string:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        try:
            # Update the project with new form data
            project.id = form.id.data
            project.title = form.title.data
            project.source = form.source.data
            project.type = form.type.data
            project.total_funding = form.total_funding.data
            project.start_year = form.start_year.data
            project.end_year = form.end_year.data
            db.session.commit()
            flash('Project updated successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating project: {e}', 'danger')
        return redirect(url_for('projects'))
    return render_template('edit_project.html', form=form)


# Delete Project
@app.route('/delete_project/<string:project_id>', methods=['POST'])
def delete_project(project_id):
    try:
        project = Project.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()
        flash('Project deleted successfully!')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting project: {e}', 'danger')
    return redirect(url_for('projects'))
