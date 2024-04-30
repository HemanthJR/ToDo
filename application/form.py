from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    completed = SelectField('completed', choices=[('select', 'select'),('False','False'), ('True', 'True')], validators=[DataRequired()])
    submit = SubmitField('submit')