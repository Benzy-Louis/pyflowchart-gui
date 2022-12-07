"""Data models"""
import flask_wtf
import wtforms

UPLOAD_FOLDER = r'uploads/'
ALLOWED_EXTENSIONS = {'py'}


class Form(flask_wtf.FlaskForm):
    """Form"""
    file = wtforms.FileField('Python file to parse',
                             id='formFile',
                             validators=[wtforms.validators.InputRequired()],
                             render_kw={'class ': 'form-control',
                                        'placeholder': 'python file to parse',
                                        'aria_label': 'python file to parse'})
    field = wtforms.StringField(
        'Field',
        render_kw={'class': 'form-control',
                            'placeholder': 'field to parse',
                            'aria_label': 'field to parse'})
    submit = wtforms.SubmitField('Submit')
