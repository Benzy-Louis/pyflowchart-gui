"""Routes and methods to manipulate requests"""
from .models import FormFile, FormField, ALLOWED_EXTENSIONS, UPLOAD_FOLDER, user_code
import flask
from pyflowchart import Flowchart
from werkzeug.utils import secure_filename
import os
controllers = flask.Blueprint('controllers', __name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def content_to_flowchart(content, field) -> str:
    """Content to flowchart"""
    try:
        flow_chart = Flowchart.from_code(
            content, field=field)
        return flow_chart.flowchart()
    except AssertionError:
        try:
            flow_chart = Flowchart.from_code(
                content, field='')
            return flow_chart.flowchart()
        except AssertionError:  # No code to parse e.g. all comments
            return ''


@controllers.route('/', methods=['GET'])
def index():
    """index route"""
    user_code.code = ''
    form_file = FormFile()
    print(form_file.errors)

    if form_file.is_submitted():
        print('/ submitted')

    if form_file.validate():
        print('/ valid')

    print(form_file.errors)
    return flask.render_template('index.html',
                                 title='pyflowchart GUI - Home', form_file=form_file)


@controllers.route('/', methods=['POST'])
def file_form():
    """index route"""
    form_file = FormFile()
    print(form_file.errors)

    if form_file.is_submitted():
        print('/ submitted')

    if form_file.validate():
        print('/ valid')

    print(form_file.errors)
    if form_file.validate_on_submit():
        file = flask.request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = f'{UPLOAD_FOLDER}{secure_filename(filename)}'
            file.save(file_path)

            with open(file_path, 'r', encoding='utf-8') as f:
                user_code.code = f.read()
            if os.path.exists(file_path):
                os.remove(file_path)
            return flask.redirect(flask.url_for('controllers.field_form'))
    return flask.redirect(flask.url_for('controllers.index'))


@ controllers.route('/parse_field', methods=['GET'])
def field_form():
    """index route"""
    form_field = FormField()
    print(form_field.errors)

    if form_field.is_submitted():
        print('/field submitted')

    if form_field.validate():
        print('/field valid')

    print(form_field.errors)
    return flask.render_template('index.html',
                                 title='pyflowchart GUI - Home', form_field=form_field, content=user_code.code)


@ controllers.route('/parse_field', methods=['POST'])
def field_form_post():
    """index route"""
    form_field = FormField()
    print(form_field.errors)

    if form_field.is_submitted():
        print('/field submitted')

    if form_field.validate():
        print('/field valid')

    print(form_field.errors)

    if form_field.validate_on_submit():
        return flask.render_template('index.html',
                                     title='pyflowchart GUI - Home', form_field=form_field, content=user_code.code, code_flowchart=content_to_flowchart(user_code.code, field=form_field.field.data))
    return flask.redirect(flask.url_for('controllers.field_form'))
