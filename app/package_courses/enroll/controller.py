
from flask import Request, flash
def validate_form(form = Request.form):

    if len(str(form.get('firstname')).replace(' ', '')) > 100:
        flash("Invalid size fro firstname", "danger")
    return True