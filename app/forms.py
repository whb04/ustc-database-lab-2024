from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired

class PaperForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    authors = StringField('Authors', validators=[DataRequired()])
    journal = StringField('Journal', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    lead = StringField('Lead', validators=[DataRequired()])
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CourseForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    teacher = StringField('Teacher', validators=[DataRequired()])
    semester = StringField('Semester', validators=[DataRequired()])
    submit = SubmitField('Submit')
