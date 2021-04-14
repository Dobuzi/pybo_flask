from flask import Blueprint, url_for, current_app
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    current_app.logger.info("print on info level")
    return redirect(url_for('question._list'))
