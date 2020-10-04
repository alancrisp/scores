from wtforms import Form
from wtforms import IntegerField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import validators
from wtforms.widgets import TextInput
from wtforms.widgets.html5 import NumberInput

class CourseForm(Form):
    name = StringField('Name', [validators.DataRequired()], widget=TextInput())
    location = StringField('Location', [validators.DataRequired()], widget=TextInput())
    city = StringField('City', [validators.DataRequired()], widget=TextInput())
    holes = IntegerField('Holes', [validators.DataRequired()], widget=NumberInput())
    submit = SubmitField('Create')
