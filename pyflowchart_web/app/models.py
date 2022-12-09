"""Data models"""
import flask_wtf
import wtforms

UPLOAD_FOLDER = r'uploads/'
ALLOWED_EXTENSIONS = {'py'}


class Code():
    """Code object to store code"""

    def __init__(self, code) -> None:
        self.code = code


class FormFile(flask_wtf.FlaskForm):
    """Form"""
    file = wtforms.FileField('Python file to parse',
                             id='formFile',
                             validators=[wtforms.validators.InputRequired()],
                             render_kw={'class ': 'form-control',
                                        'placeholder': 'python file to parse',
                                        'aria_label': 'python file to parse'})
    submit = wtforms.SubmitField(
        'Submit', render_kw={'class': 'btn btn-info'})


class FormField(flask_wtf.FlaskForm):
    field = wtforms.StringField(
        'Field',
        render_kw={'class': 'form-control',
                            'placeholder': 'field to parse',
                            'aria_label': 'field to parse'})
    submit = wtforms.SubmitField(
        'Process', render_kw={'class': 'btn btn-info'})


user_code = Code('')
