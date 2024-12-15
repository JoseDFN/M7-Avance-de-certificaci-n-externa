from flask import Blueprint

bp = Blueprint('todo', __name__, url_prefix = '/todo')

@bp.route('/list')
def index():
    return 'To-do list'

@bp.route('/create')
def create():
    return 'Create a new to-do item'