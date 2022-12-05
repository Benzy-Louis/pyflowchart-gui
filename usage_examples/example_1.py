from pyflowchart import Flowchart
with open(r'C:\Users\BCPL7514\DEV-ALT\developer-institute-js-python-bootcamp\week_2\day_4\follow_along\exercise_2.py') as f:
    code = f.read()

fc = Flowchart.from_code(code, field='Computer')
print(fc.flowchart())

# output flowchart code.
