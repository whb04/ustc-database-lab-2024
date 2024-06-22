# app/routes.py

from flask import render_template, redirect, url_for, flash, request, make_response
import csv
import io
from app import app, db
from app.models import Teacher, Paper, Course, Project, TeacherPaper, TeacherCourse, TeacherProject
from app.forms import TeacherForm, PaperForm, CourseForm, ProjectForm, PaperAuthorForm, CourseTeacherForm, ProjectTeacherForm, TeacherQueryForm

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
    author_form = PaperAuthorForm()
    if form.validate_on_submit():
        try:
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
        return redirect(url_for('edit_paper', paper_id=paper.id))
    return render_template('edit_paper.html', form=form, author_form=author_form, paper=paper)

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

@app.route('/add_paper_author/<int:paper_id>', methods=['POST'])
def add_paper_author(paper_id):
    form = PaperAuthorForm()
    paper = Paper.query.get_or_404(paper_id)
    if form.validate_on_submit():
        try:
            if form.is_corresponding_author.data and TeacherPaper.query.filter_by(paper_id=paper_id, is_corresponding_author=True).count() > 0:
                flash('Only one corresponding author is allowed per paper.', 'danger')
            elif TeacherPaper.query.filter_by(paper_id=paper_id, rank=form.rank.data).count() > 0:
                flash('Author ranks must be unique.', 'danger')
            else:
                author = TeacherPaper(
                    paper_id=paper_id,
                    teacher_id=form.teacher_id.data,
                    rank=form.rank.data,
                    is_corresponding_author=form.is_corresponding_author.data
                )
                db.session.add(author)
                db.session.commit()
                flash('Author added successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding author: {e}', 'danger')
    return redirect(url_for('edit_paper', paper_id=paper_id))

@app.route('/delete_paper_author/<int:paper_id>/<string:teacher_id>', methods=['POST'])
def delete_paper_author(paper_id, teacher_id):
    author = TeacherPaper.query.filter_by(paper_id=paper_id, teacher_id=teacher_id).first_or_404()
    try:
        db.session.delete(author)
        db.session.commit()
        flash('Author deleted successfully!')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting author: {e}', 'danger')
    return redirect(url_for('edit_paper', paper_id=paper_id))

# Edit Course
@app.route('/edit_course/<string:course_id>', methods=['GET', 'POST'])
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    form = CourseForm(obj=course)
    teacher_form = CourseTeacherForm()
    if form.validate_on_submit():
        try:
            course.id = form.id.data
            course.title = form.title.data
            course.hours = form.hours.data
            course.nature = form.nature.data
            db.session.commit()
            flash('Course updated successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating course: {e}', 'danger')
        return redirect(url_for('edit_course', course_id=course.id))
    return render_template('edit_course.html', form=form, teacher_form=teacher_form, course=course)

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

@app.route('/add_course_teacher/<string:course_id>', methods=['POST'])
def add_course_teacher(course_id):
    form = CourseTeacherForm()
    course = Course.query.get_or_404(course_id)
    if form.validate_on_submit():
        try:
            teacher_course = TeacherCourse(
                course_id=course_id,
                teacher_id=form.teacher_id.data,
                year=form.year.data,
                semester=form.semester.data,
                hours_taken=form.hours_taken.data
            )
            db.session.add(teacher_course)
            db.session.commit()
            flash('Teacher added successfully!')
        except Exception as e:
            db.session.rollback()
            print(f'Error adding teacher: {e}')
            flash(f'Error adding teacher: {e}', 'danger')
    else:
        print(form.errors)
    return redirect(url_for('edit_course', course_id=course_id))

@app.route('/delete_course_teacher/<string:course_id>/<string:teacher_id>', methods=['POST'])
def delete_course_teacher(course_id, teacher_id):
    teacher_course = TeacherCourse.query.filter_by(course_id=course_id, teacher_id=teacher_id).first_or_404()
    try:
        db.session.delete(teacher_course)
        db.session.commit()
        flash('Teacher deleted successfully!')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting teacher: {e}', 'danger')
    return redirect(url_for('edit_course', course_id=course_id))

# Edit Project
@app.route('/edit_project/<string:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    form = ProjectForm(obj=project)
    teacher_form = ProjectTeacherForm()
    if form.validate_on_submit():
        try:
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
        return redirect(url_for('edit_project', project_id=project.id))
    return render_template('edit_project.html', form=form, teacher_form=teacher_form, project=project)

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

@app.route('/add_project_teacher/<string:project_id>', methods=['POST'])
def add_project_teacher(project_id):
    form = ProjectTeacherForm()
    project = Project.query.get_or_404(project_id)
    if form.validate_on_submit():
        try:
            if TeacherProject.query.filter_by(project_id=project_id, rank=form.rank.data).count() > 0:
                flash('Teacher ranks must be unique.', 'danger')
            else:
                teacher_project = TeacherProject(
                    project_id=project_id,
                    teacher_id=form.teacher_id.data,
                    rank=form.rank.data,
                    funding_taken=form.funding_taken.data
                )
                db.session.add(teacher_project)
                db.session.commit()
                flash('Teacher added successfully!')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding teacher: {e}', 'danger')
    return redirect(url_for('edit_project', project_id=project_id))

@app.route('/delete_project_teacher/<string:project_id>/<string:teacher_id>', methods=['POST'])
def delete_project_teacher(project_id, teacher_id):
    teacher_project = TeacherProject.query.filter_by(project_id=project_id, teacher_id=teacher_id).first_or_404()
    try:
        db.session.delete(teacher_project)
        db.session.commit()
        flash('Teacher deleted successfully!')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting teacher: {e}', 'danger')
    return redirect(url_for('edit_project', project_id=project_id))

@app.route('/teacher_summary', methods=['GET', 'POST'])
def teacher_summary():
    form = TeacherQueryForm()
    teacher = None
    courses = []
    papers = []
    projects = []

    if form.validate_on_submit():
        teacher_id = form.teacher_id.data
        start_year = form.start_year.data
        end_year = form.end_year.data
        
        teacher = Teacher.query.get(teacher_id)
        if teacher:
            courses = TeacherCourse.query.filter(
                TeacherCourse.teacher_id == teacher_id,
                TeacherCourse.year.between(start_year, end_year)
            ).all()
            papers = TeacherPaper.query.join(Paper).filter(
                TeacherPaper.teacher_id == teacher_id,
                Paper.year.between(start_year, end_year)
            ).all()
            projects = TeacherProject.query.join(Project).filter(
                TeacherProject.teacher_id == teacher_id,
                Project.start_year <= end_year,
                Project.end_year >= start_year
            ).all()
        else:
            flash(f'Teacher with ID {teacher_id} not found.', 'danger')

    return render_template('teacher_summary.html', form=form, teacher=teacher, courses=courses, papers=papers, projects=projects)

@app.route('/export_teacher_summary', methods=['GET', 'POST'])
def export_teacher_summary():
    form = TeacherQueryForm()
    if form.validate_on_submit():
        teacher_id = form.teacher_id.data
        start_year = form.start_year.data
        end_year = form.end_year.data

        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            flash(f'Teacher with ID {teacher_id} not found.', 'danger')
            return redirect(url_for('teacher_summary'))

        courses = TeacherCourse.query.filter(
            TeacherCourse.teacher_id == teacher_id,
            TeacherCourse.year.between(start_year, end_year)
        ).all()
        papers = TeacherPaper.query.join(Paper).filter(
            TeacherPaper.teacher_id == teacher_id,
            Paper.year.between(start_year, end_year)
        ).all()
        projects = TeacherProject.query.join(Project).filter(
            TeacherProject.teacher_id == teacher_id,
            Project.start_year <= end_year,
            Project.end_year >= start_year
        ).all()

        # Generate CSV
        output = io.StringIO()
        writer = csv.writer(output)

        # Write teacher info
        writer.writerow(['教师基本信息'])
        writer.writerow(['工号', '姓名', '性别', '职称'])
        writer.writerow([teacher.id, teacher.name, '男' if teacher.gender == 1 else '女', teacher.title])

        # Write teaching info
        writer.writerow([])
        writer.writerow(['教学情况'])
        writer.writerow(['课程序号', '课程名称', '主讲学时', '学期'])
        for course in courses:
            writer.writerow([course.course_id, course.course.title, course.hours_taken, course.semester])

        # Write papers info
        writer.writerow([])
        writer.writerow(['发表论文情况'])
        writer.writerow(['序号', '论文名称', '发表源', '发表年份', '类型', '级别', '排名', '是否通讯作者'])
        for paper in papers:
            writer.writerow([paper.paper_id, paper.paper.title, paper.paper.source, paper.paper.year, paper.paper.type, paper.paper.level, paper.rank, '是' if paper.is_corresponding_author else '否'])

        # Write projects info
        writer.writerow([])
        writer.writerow(['承担项目情况'])
        writer.writerow(['项目号', '项目名称', '项目来源', '项目类型', '总经费', '开始年份', '结束年份', '排名', '承担经费'])
        for project in projects:
            writer.writerow([project.project_id, project.project.title, project.project.source, project.project.type, project.project.total_funding, project.project.start_year, project.project.end_year, project.rank, project.funding_taken])

        # Create response
        response = make_response(output.getvalue())
        response.headers['Content-Disposition'] = f'attachment; filename={teacher_id}_summary_{start_year}-{end_year}.csv'
        response.headers['Content-type'] = 'text/csv'
        return response
    else:
        print(form.errors)

    return render_template('teacher_summary.html', form=form)
