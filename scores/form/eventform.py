from wtforms import Form
from wtforms import StringField
from wtforms import SelectField
from wtforms import SubmitField
from wtforms import validators
from wtforms.widgets.html5 import DateInput

class EventForm(Form):
    course = SelectField('Course', [validators.InputRequired()], coerce=int, validate_choice=False)
    date = StringField('Date', [validators.InputRequired()], widget=DateInput())
    submit = SubmitField('Create')
