import flask_wtf
import wtforms


# class Form(flask_wtf.FlaskForm):
#     first_name = wtforms.StringField(
#         "firstName", [wtforms.validators.Length(min=4, max=25,message="Hey mett enn nom au moins 4 lett do!")]
#     )
#     last_name = wtforms.StringField(
#         "lastName", [wtforms.validators.Length(min=4, max=25)]
#     )
#     age = wtforms.IntegerField("age", [wtforms.validators.NumberRange(min=0, max=999)])
#     submit = wtforms.SubmitField("Submit")
