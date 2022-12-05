import flask
from app import app
from app import forms


from pyflowchart import Flowchart


@app.route("/")
def index():
    """index"""
    with open(r'C:\Users\BCPL7514\DEV-ALT\developer-institute-js-python-bootcamp\week_2\day_4\follow_along\exercise_2.py') as f:
        code = f.read()
    fc = Flowchart.from_code(code, field='Computer')
    code_flowchart = fc.flowchart()
    return flask.render_template("index.html", code_flowchart=code_flowchart)
