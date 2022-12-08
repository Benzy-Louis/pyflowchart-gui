"""Routes and methods to manipulate requests"""
from .models import Form, ALLOWED_EXTENSIONS, UPLOAD_FOLDER
import flask
from pyflowchart import Flowchart
from werkzeug.utils import secure_filename
import os
controllers = flask.Blueprint('controllers', __name__)
# @controllers.route("/")
# def index():
#     """index"""
#     root_path = r'C:\Users\BCPL7514\DEV-ALT\developer-institute-js-python-bootcamp'
#     print(root_path)
#     file_path = rf'{root_path}\week_2\day_2\ExercisesXP\exercise_4.py'
#     print(file_path)
#     with open(file_path, encoding='utf-8') as file:
#         code = file.read()
#     flow_chart = Flowchart.from_code(code, field='')
#     code_flowchart = flow_chart.flowchart()
#     return flask.render_template("example_flowchart_js.html",
#                                  code_flowchart=code_flowchart,
#                                  code=code)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@controllers.route("/", methods=['GET', 'POST'])
def index():
    """index route"""
    form = Form()
    # if form.validate_on_submit():
    #     file = flask.request.files['file']
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file_path = f"{UPLOAD_FOLDER}{secure_filename(filename)}"
    #         file.save(file_path)

    #         # content_stream = file.stream
    #         # Open the file for writing.
    #         with open(content_stream.name, 'r') as f:
    #             # where `stuff` is, y'know... stuff to write (a string)
    #             content = content_stream.read()

    #         # with open(file_path, "r", encoding='utf-8') as f:
    #         #     content = f.read()
    #         # flow_chart = Flowchart.from_code(content, field='')
    #         # code_flowchart = flow_chart.flowchart()
    #         code_flowchart = ''
    #         return flask.render_template("index.html",
    #                                      title="pyflowchart GUI", form=form,
    #                                      content=content,
    #                                      code_flowchart=code_flowchart)
    #         # return flask.render_template("example_flowchart_js.html",
    #         #                              #  title="pyflowchart GUI", form=form,
    #         #                              code=content,
    #         #                              code_flowchart=code_flowchart)
    return flask.render_template("index.html",
                                 title="pyflowchart GUI", form=form)
