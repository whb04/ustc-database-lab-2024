# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, DateField, SubmitField
from wtforms.validators import DataRequired

class TeacherForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    gender = IntegerField('Gender', validators=[DataRequired()])
    title = IntegerField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PaperForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    source = StringField('Source', validators=[DataRequired()])
    year = DateField('Year', validators=[DataRequired()])
    type = IntegerField('Type', validators=[DataRequired()])
    level = IntegerField('Level', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CourseForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    hours = IntegerField('Hours', validators=[DataRequired()])
    nature = IntegerField('Nature', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProjectForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    source = StringField('Source', validators=[DataRequired()])
    type = IntegerField('Type', validators=[DataRequired()])
    total_funding = FloatField('Total Funding', validators=[DataRequired()])
    start_year = IntegerField('Start Year', validators=[DataRequired()])
    end_year = IntegerField('End Year', validators=[DataRequired()])
    submit = SubmitField('Submit')
