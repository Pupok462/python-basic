from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    name = StringField(
        validators=[
            DataRequired(),
            Length(min=3),
        ]
    )
    username = StringField(
        validators=[
            DataRequired(),
            Length(min=1)
        ]
    )
    email = StringField(
        validators=[
            DataRequired(),
            Length(min=5)
        ]
    )
