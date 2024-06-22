# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TeacherForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[(1, '男'), (2, '女')], coerce=int, validators=[DataRequired()])
    title = SelectField('Title', choices=[
        (1, '博士后'), (2, '助教'), (3, '讲师'), (4, '副教授'), (5, '特任教授'), 
        (6, '教授'), (7, '助理研究员'), (8, '特任副研究员'), (9, '副研究员'), 
        (10, '特任研究员'), (11, '研究员')], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')

class PaperForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    source = StringField('Source', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    type = SelectField('Type', choices=[
        (1, 'full paper'), (2, 'short paper'), (3, 'poster paper'), (4, 'demo paper')], 
        coerce=int, validators=[DataRequired()])
    level = SelectField('Level', choices=[
        (1, 'CCF-A'), (2, 'CCF-B'), (3, 'CCF-C'), (4, '中文CCF-A'), 
        (5, '中文CCF-B'), (6, '无级别')], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')

class PaperAuthorForm(FlaskForm):
    teacher_id = StringField('Teacher ID', validators=[DataRequired()])
    rank = IntegerField('Rank', validators=[DataRequired()])
    is_corresponding_author = BooleanField('Corresponding Author')
    submit = SubmitField('Add Author')

class CourseForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    hours = IntegerField('Hours', validators=[DataRequired()])
    nature = SelectField('Nature', choices=[(1, '本科生课程'), (2, '研究生课程')], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')

class CourseTeacherForm(FlaskForm):
    teacher_id = StringField('Teacher ID', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    semester = SelectField('Semester', choices=[(1, '春季学期'), (2, '夏季学期'), (3, '秋季学期')], coerce=int, validators=[DataRequired()])
    hours_taken = IntegerField('Hours', validators=[DataRequired()])
    submit = SubmitField('Add Teacher')

class ProjectForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    source = StringField('Source', validators=[DataRequired()])
    type = SelectField('Type', choices=[
        (1, '国家级项目'), (2, '省部级项目'), (3, '市厅级项目'), (4, '企业合作项目'), 
        (5, '其它类型项目')], coerce=int, validators=[DataRequired()])
    total_funding = FloatField('Total Funding', validators=[DataRequired()])
    start_year = IntegerField('Start Year', validators=[DataRequired()])
    end_year = IntegerField('End Year', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProjectTeacherForm(FlaskForm):
    teacher_id = StringField('Teacher ID', validators=[DataRequired()])
    rank = IntegerField('Rank', validators=[DataRequired()])
    funding_taken = FloatField('Funding', validators=[DataRequired()])
    submit = SubmitField('Add Teacher')

class TeacherQueryForm(FlaskForm):
    teacher_id = StringField('Teacher ID', validators=[DataRequired()])
    start_year = IntegerField('Start Year', validators=[DataRequired()])
    end_year = IntegerField('End Year', validators=[DataRequired()])
    submit = SubmitField('Query')