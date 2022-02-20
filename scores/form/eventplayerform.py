from wtforms import Form
from wtforms import HiddenField
from wtforms import SelectField
from wtforms import SubmitField
from wtforms import validators

class EventPlayerForm(Form):
    eventId = HiddenField()
    player = SelectField('Player', [validators.InputRequired()], coerce=int, validate_choice=False)
    submit = SubmitField('Add Player')
