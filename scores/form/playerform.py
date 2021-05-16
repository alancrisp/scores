from wtforms import Form
from wtforms import StringField
from wtforms import SubmitField
from wtforms import validators
from wtforms.widgets import TextInput

class PlayerForm(Form):
    name = StringField('Name', [validators.DataRequired()], widget=TextInput())
    submit = SubmitField('Create')
