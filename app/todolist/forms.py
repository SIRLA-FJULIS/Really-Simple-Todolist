from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField
from wtforms.validators import DataRequired
import datetime

class ToDoListForm(FlaskForm):
    date = DateField('Date', default=datetime.date.today(), format='%Y-%m-%d', validators=[DataRequired()])
    item = StringField('Item', validators=[DataRequired()])
    submit = SubmitField('Submit')