import flask
from app import app
from app import forms


from pyflowchart import Flowchart


@app.route("/")
def index():
    """index"""
    with open(r'/Users/rubenlouis/DEV/BOOTCAMPS/developer-institute-js-python-bootcamp/week_2/day_4/DailyChallenge/exercise_1.py') as f:
        code = f.read()
    fc = Flowchart.from_code(code, field='')
    code_flowchart = fc.flowchart()
    return flask.render_template("example_flowchart_js.html", code_flowchart=code_flowchart, code=code)

