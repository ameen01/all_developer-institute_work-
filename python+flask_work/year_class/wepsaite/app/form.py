from flask_wtf import FlaskForm
from wtforms import SelectField, TextField,SubmitField

class AddForm(FlaskForm):
    catogary = SelectField(label=)