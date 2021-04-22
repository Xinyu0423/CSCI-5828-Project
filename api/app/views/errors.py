from flask import Blueprint

errors = Blueprint('errors', __name__)

@errors.errorhandler(404)
def page_not_found(e):
    return "Error."