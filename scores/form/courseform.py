from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField

class CourseForm(Form):
    name = StringField('Name')
    location = StringField('Location')
    city = StringField('City')
    holes = IntegerField('holes')
